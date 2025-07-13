import tkinter as tk
from tkinter import messagebox
import subprocess
from docx import Document
from datetime import datetime
import os
import webbrowser
import urllib.parse
import win32com.client
import locale
import tempfile
import shutil
from tkcalendar import Calendar

# idioma#
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')  # Linux/Unix
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')  # Windows
    except locale.Error:
        pass

def abrir_arquivo(caminho):
    print(f"Tentando abrir o arquivo: {caminho}")
    try:
        subprocess.run(['start', '', caminho], shell=True, check=True)
        print("Arquivo aberto com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao abrir arquivo: {e}")
        messagebox.showerror("Erro", f"Não foi possível abrir o arquivo: {e}")

def abrir_programa():
    try:
        caminho_exe = os.path.join(os.path.dirname(__file__), "dist", "contrato_app.exe")
        subprocess.Popen([caminho_exe])
        label_status.config(text="Programa aberto com sucesso!")
    except FileNotFoundError:
        label_status.config(text="Erro: Programa não encontrado.")
    except Exception as e:
        label_status.config(text=f"Erro ao abrir o programa: {e}")

def escolher_data():
    def pegar_data():
        data_selecionada = cal.selection_get()
        data_formatada = data_selecionada.strftime("%d/%m/%Y")
        entradas["campo_data_contrato"].delete(0, tk.END)
        entradas["campo_data_contrato"].insert(0, data_formatada)
        top.destroy()

    top = tk.Toplevel(janela)
    top.title("Selecionar Data do Contrato")
    cal = Calendar(top, locale='pt_BR', date_pattern='dd/mm/yyyy')
    cal.pack(padx=10, pady=10)

    btn_ok = tk.Button(top, text="OK", command=pegar_data)
    btn_ok.pack(pady=10)

def formatar_data_contrato(data_manual):
    if data_manual.strip():
        try:
            data_dt = datetime.strptime(data_manual.strip(), "%d/%m/%Y")
        except ValueError:
            return None
    else:
        data_dt = datetime.now()
    mes_minusculo = data_dt.strftime("%B").lower()
    return f"Curitiba, {data_dt.day} de {mes_minusculo} de {data_dt.year}"

def criar_documento(nome, endereco, cep, telefone, horario, local_evento,
                    valor_pessoa, valor_total, valor_entrada, data_contrato, itens_selecionados):
    doc = Document()
    p = doc.add_paragraph()
    run = p.add_run("CONTRATO DE PRESTAÇÃO DE SERVIÇOS")
    run.bold = True

    p = doc.add_paragraph()
    p.add_run("CONTRATANTE:\n").bold = True
    p.add_run(f"Nome: {nome}\nTelefone: {telefone}\nEndereço: {endereco}\nCEP: {cep}\nHorário do Evento: {horario}\nLocal do Evento: {local_evento}")

    p = doc.add_paragraph()
    p.add_run("\nCONTRATADA:\n").bold = True
    p.add_run(
        "**MARIANA SOUZA DA COSTA**, brasileira, solteira, chef de cozinha, \n"
"nascida em 20/03/1990, natural de Londrina, PR, residente e domiciliada na cidade de Curitiba, PR, \n"
"na Rua das Acácias, 123 – Jardim Botânico, CEP 80240-120, \n"
"portadora do RG 12345678-9 SSP/PR, CPF nº 123.456.789-00; microempreendedora individual (ME), \n"
"sob o nome empresarial 12.345.678 MARIANA SOUZA DA COSTA, \n"
"com sede na mesma cidade, inscrita na Junta Comercial sob o NIRE 4180000000-0 \n"
"e no CNPJ sob o nº 12.345.678/0001-99."

    )

    p = doc.add_paragraph()
    p.add_run("OBJETO DO CONTRATO").bold = True
    p = doc.add_paragraph("Cardápio:", style='Heading2')

    # Adiciona os itens selecionados usando lista com marcadores
    for item in itens_selecionados:
        doc.add_paragraph(item, style='List Bullet')

    doc.add_paragraph(f"\nValor: R$ {valor_pessoa} por pessoa, com deslocamento incluso, montagem e copeira durante o evento para servir.")

    clausulas = [
        "Cláusula 2ª. O CONTRATANTE deverá fornecer todas as informações necessárias à realização do serviço.",
        "Cláusula 3ª. O CONTRATANTE deverá efetuar o pagamento conforme cláusula 6ª.",
        "Cláusula 4ª. O CONTRATADO entregará uma cópia do contrato ao contratante.",
        "Cláusula 5ª. O CONTRATADO fornecerá recibo referente aos pagamentos efetuados.",
        f"Cláusula 6ª. O serviço será remunerado em R$ {valor_total}, com entrada de R$ {valor_entrada} e o restante no evento. Pagamento via PIX, crédito ou débito.",
        "Cláusula 7ª. Inadimplemento gera multa de 10%, juros de 10% ao mês e correção monetária.",
        "Cláusula 8ª. Descumprimento gera multa de 30% do valor total.",
        "Cláusula 9ª. Rescisão imotivada exige aviso prévio de 30 dias.",
        "Cláusula 10ª. Se o CONTRATANTE cancelar, devolve-se 50% do valor total.",
        "Cláusula 11ª. Se o CONTRATADO cancelar, deve devolver 100% do valor referente aos serviços não prestados.",
        "Cláusula 12ª. O serviço será realizado conforme prazos estabelecidos neste contrato.",
        "Cláusula 13ª. Não existe vínculo empregatício entre as partes.",
        "Cláusula 14ª. Não é permitida subcontratação sem autorização do CONTRATADO."
    ]
    for c in clausulas:
        doc.add_paragraph(c)

    doc.add_paragraph("\nPor estarem assim justos e contratados, firmam o presente instrumento em duas vias de igual teor.")
    doc.add_paragraph(f"\n{data_contrato}.")

    tabela = doc.add_table(rows=2, cols=2)
    tabela.cell(0, 0).text = "Daniela Rodrigues"
    tabela.cell(1, 0).text = "_____________________"
    tabela.cell(0, 1).text = "Assinatura do Contratante"
    tabela.cell(1, 1).text = "_____________________"

    return doc

def salvar_dados(nome, endereco, cep, telefone, horario, local_evento,
                 valor_pessoa, valor_total, valor_entrada, data_manual, itens_selecionados):

    print("Itens selecionados para salvar:", itens_selecionados)  # <<<<<< DEBUG AQUI

    if not nome.strip() or not endereco.strip() or not cep.strip() or not telefone.strip() or not horario.strip() or not local_evento.strip():
        messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
        return
    if not valor_pessoa.strip() or not valor_total.strip() or not valor_entrada.strip():
        messagebox.showerror("Erro", "Informe os valores financeiros corretamente.")
        return
    if len(itens_selecionados) == 0:
        messagebox.showerror("Erro", "Selecione pelo menos um item do cardápio.")
        return

    data_contrato = formatar_data_contrato(data_manual)
    if data_contrato is None:
        messagebox.showerror("Erro", "Data do contrato inválida. Use dd/mm/aaaa.")
        return

    doc = criar_documento(nome, endereco, cep, telefone, horario, local_evento,
                          valor_pessoa, valor_total, valor_entrada, data_contrato, itens_selecionados)

    pasta_base = os.path.join(os.path.expanduser("~"), "contrato_app")
    pasta_word = os.path.join(pasta_base, "Word")
    pasta_pdf = os.path.join(pasta_base, "PDF")
    os.makedirs(pasta_word, exist_ok=True)
    os.makedirs(pasta_pdf, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_base = f"contrato_{nome}_{timestamp}"
    caminho_docx = os.path.join(pasta_word, nome_base + ".docx")
    caminho_pdf = os.path.join(pasta_pdf, nome_base + ".pdf")
#word abrir #
    doc.save(caminho_docx)

    try:
        word_app = win32com.client.Dispatch("Word.Application")
        word_app.Visible = False
        doc_pdf = word_app.Documents.Open(caminho_docx)
        doc_pdf.SaveAs(caminho_pdf, FileFormat=17)
        doc_pdf.Close()
        word_app.Quit()
        abrir_arquivo(caminho_pdf)
    except Exception as e:
        messagebox.showwarning("Aviso", f"Erro ao converter para PDF: {e}")
        abrir_arquivo(caminho_docx)
#link whatsapp#
    numero = telefone.strip().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    msg = f"Olá {nome}, segue o contrato gerado em {data_contrato}."
    texto_url = urllib.parse.quote(msg)
    link = f"https://wa.me/55{numero}?text={texto_url}"
    webbrowser.open(link)

def visualizar_contrato_temporario(nome, endereco, cep, telefone, horario, local_evento,
                                  valor_pessoa, valor_total, valor_entrada, data_manual, itens_selecionados):

    print("Itens selecionados para visualizar:", itens_selecionados)  # <<<<<< DEBUG AQUI

    if not nome.strip() or not endereco.strip() or not cep.strip() or not telefone.strip() or not horario.strip() or not local_evento.strip():
        messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
        return
    if not valor_pessoa.strip() or not valor_total.strip() or not valor_entrada.strip():
        messagebox.showerror("Erro", "Informe os valores financeiros corretamente.")
        return
    if len(itens_selecionados) == 0:
        messagebox.showerror("Erro", "Selecione pelo menos um item do cardápio.")
        return

    data_contrato = formatar_data_contrato(data_manual)
    if data_contrato is None:
        messagebox.showerror("Erro", "Data do contrato inválida. Use dd/mm/aaaa.")
        return

    with tempfile.TemporaryDirectory() as tmpdirname:
        caminho_docx = os.path.join(tmpdirname, "contrato_preview.docx")
        doc = criar_documento(nome, endereco, cep, telefone, horario, local_evento,
                              valor_pessoa, valor_total, valor_entrada, data_contrato, itens_selecionados)
        doc.save(caminho_docx)

        try:
            abrir_arquivo(caminho_docx)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o documento para visualização: {e}")
            return

        resposta = messagebox.askyesno("Salvar Contrato", "Deseja salvar este contrato definitivamente?")
        if resposta:
            pasta_base = os.path.join(os.path.expanduser("~"), "contrato_app")
            pasta_word = os.path.join(pasta_base, "Word")
            pasta_pdf = os.path.join(pasta_base, "PDF")
            os.makedirs(pasta_word, exist_ok=True)
            os.makedirs(pasta_pdf, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nome_base = f"contrato_{nome}_{timestamp}"
            caminho_docx_final = os.path.join(pasta_word, nome_base + ".docx")
            caminho_pdf_final = os.path.join(pasta_pdf, nome_base + ".pdf")

            shutil.copy(caminho_docx, caminho_docx_final)

            try:
                word_app = win32com.client.Dispatch("Word.Application")
                word_app.Visible = False
                doc_pdf = word_app.Documents.Open(caminho_docx_final)
                doc_pdf.SaveAs(caminho_pdf_final, FileFormat=17)
                doc_pdf.Close()
                word_app.Quit()
                abrir_arquivo(caminho_pdf_final)
                messagebox.showinfo("Sucesso", f"Contrato salvo em:\n{caminho_docx_final} e {caminho_pdf_final}")
            except Exception as e:
                messagebox.showwarning("Aviso", f"Erro ao converter para PDF: {e}")
                abrir_arquivo(caminho_docx_final)
        else:
            messagebox.showinfo("Cancelado", "Contrato não salvo.")

# Interface gráfica
janela = tk.Tk()
janela.title("Cadastro de Clientes e Cardápio")
janela.geometry("600x800")
janela.resizable(True, True)
#dados cliente#
campos = [
    ("Nome:", "campo_nome"),
    ("Endereço:", "campo_endereco"),
    ("CEP:", "campo_cep"),
    ("Telefone:", "campo_telefone"),
    ("Horário do Evento:", "campo_horario"),
    ("Local do Evento:", "campo_local"),
    ("Valor por Pessoa (R$):", "campo_valor_pessoa"),
    ("Valor Total (R$):", "campo_valor_total"),
    ("Valor Entrada (R$):", "campo_valor_entrada"),
    ("Data do Contrato (dd/mm/aaaa):", "campo_data_contrato")
]

entradas = {}
for i, (rotulo, nome_var) in enumerate(campos):
    tk.Label(janela, text=rotulo).grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)
    e = tk.Entry(janela, width=50)
    e.grid(row=i, column=1, padx=5, pady=5, sticky=tk.EW)
    entradas[nome_var] = e

janela.grid_columnconfigure(1, weight=1)

entradas["campo_valor_pessoa"].insert(0, "39,90")
entradas["campo_valor_total"].insert(0, "3987,00")
entradas["campo_valor_entrada"].insert(0, "1993,50")

btn_calendario = tk.Button(janela, text="📅", width=3, command=escolher_data)
btn_calendario.grid(row=len(campos)-1, column=2, padx=5, pady=5)

tk.Label(janela, text="Selecione os itens do cardápio:").grid(row=10, column=0, columnspan=2, sticky=tk.W, padx=5, pady=10)
#cardapio#
itens = [
    "folheado de queijo", "pão de queijo", "1 tipo de quiche", "quibe", "coxinha",
    "Bolinha de queijo", "Sanduíche de brioche e pão", "frios e alface americana",
    "Suco de laranja", "Café", "Leite", "Café cremoso"
]

vars_itens = []
for i, item in enumerate(itens):
    var = tk.IntVar()
    c = tk.Checkbutton(janela, text=item, variable=var)
    c.grid(row=11 + i, column=0, columnspan=2, sticky=tk.W, padx=20)
    vars_itens.append((item, var))

frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=11 + len(itens), column=0, columnspan=2, pady=10, sticky=tk.EW)

botao_visualizar = tk.Button(frame_botoes, text="Visualizar Contrato", command=lambda: (
    print("Itens selecionados (botão visualizar):", [item for item, var in vars_itens if var.get() == 1]),
    visualizar_contrato_temporario(
        entradas["campo_nome"].get(),
        entradas["campo_endereco"].get(),
        entradas["campo_cep"].get(),
        entradas["campo_telefone"].get(),
        entradas["campo_horario"].get(),
        entradas["campo_local"].get(),
        entradas["campo_valor_pessoa"].get(),
        entradas["campo_valor_total"].get(),
        entradas["campo_valor_entrada"].get(),
        entradas["campo_data_contrato"].get(),
        [item for item, var in vars_itens if var.get() == 1]
    )
))
botao_visualizar.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

botao_salvar = tk.Button(frame_botoes, text="Salvar Contrato", command=lambda: (
    print("Itens selecionados (botão salvar):", [item for item, var in vars_itens if var.get() == 1]),
    salvar_dados(
        entradas["campo_nome"].get(),
        entradas["campo_endereco"].get(),
        entradas["campo_cep"].get(),
        entradas["campo_telefone"].get(),
        entradas["campo_horario"].get(),
        entradas["campo_local"].get(),
        entradas["campo_valor_pessoa"].get(),
        entradas["campo_valor_total"].get(),
        entradas["campo_valor_entrada"].get(),
        entradas["campo_data_contrato"].get(),
        [item for item, var in vars_itens if var.get() == 1]
    )
))
botao_salvar.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
#entrada apagar dados#
def limpar_campos():
    for entrada in entradas.values():
        entrada.delete(0, tk.END)
    for _, var in vars_itens:
        var.set(0)
    label_status.config(text="Campos limpos.")

botao_limpar = tk.Button(frame_botoes, text="Limpar Campos", command=limpar_campos)
botao_limpar.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

botao_abrir = tk.Button(janela, text="Abrir Programa", command=abrir_programa)
botao_abrir.grid(row=12 + len(itens), column=0, columnspan=2, pady=5, sticky=tk.EW)

label_status = tk.Label(janela, text="")
label_status.grid(row=13 + len(itens), column=0, columnspan=2)

janela.mainloop()
