from pywinauto.application import Application

def open_code_blocks():
    app = Application().start('notepad.exe')
    app.UntiledNotepad.Edit.type_keys("Teste de automação com pywinauto - Turma Super Dev - RPA  em Pywinauto", with_spaces=True)
    app.UntiledNotepad.menu_select("Salvar->Arquivo")
    app.SaveAs.ComboBox5.select("UTF-8")
    app.SaveAs.edit1.set_text("Escrita1.txt")
    app.SaveAs.Save.click()

open_code_blocks()
