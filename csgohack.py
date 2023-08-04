from pymem.process import *
import customtkinter as ctk
from time import sleep
from pymem import *
import webbrowser
import keyboard
import win32gui
texto_da_janela = win32gui.FindWindow(None, 'Counter-Strike: Global Offensive - Direct3D 9')
if texto_da_janela:


    def GetPtrAddr(base, offsets):
        endereço = processo.read_int(base)
        for offset in offsets:
            if offset != offsets[-1]:
                endereço = processo.read_int(endereço + offset)
        return endereço + offsets[-1]


    processo = pymem.Pymem('csgo.exe')
    endereço_base = module_from_name(processo.process_handle, 'client.dll').lpBaseOfDll
    valor_do_endereço_do_wallhack = processo.read_int(endereço_base + 0xDE5670)
    valor_do_endereço_do_grenadepreview = processo.read_int(endereço_base + 0xE06C38)
    valor_do_endereço_do_glow_das_armas_no_chão = processo.read_int(endereço_base + 0xDFD4D8)
    janela = ctk.CTk()
    janela.title('External Hack For CS:GO')
    janela.geometry('380x220')
    janela.resizable(width=False, height=False)


    def abrir_link():
        url = "https://tiago.fun/"
        webbrowser.open(url)


    def wallhack():
        if switch_do_wallhack.get() == 1:
            processo.write_int(endereço_base + 0xDE5670, valor_do_endereço_do_wallhack + 1)
        else:
            processo.write_int(endereço_base + 0xDE5670, valor_do_endereço_do_wallhack)


    def auto_bhop_normal():
        if switch_do_auto_bhop_normal.get() == 1:
            local_player = GetPtrAddr(endereço_base + 0x0525BE24, [0x9C, 0x48, 0x0, 0x100])
            force_jump = endereço_base + 0x52BBCD8
            parada = local_player + 4
            endereço_da_parada = processo.read_int(parada)
            if keyboard.is_pressed('space'):
                if endereço_da_parada == 257:
                    processo.write_int(force_jump, 6)
                    sleep(0.01)
                    processo.write_int(force_jump, 4)
        janela.after(1, auto_bhop_normal)


    def auto_bhop_agachado():
        if switch_do_auto_bhop_agachado.get() == 1:
            local_player = GetPtrAddr(endereço_base + 0x0525BE24, [0x9C, 0x48, 0x0, 0x100])
            force_jump = endereço_base + 0x52BBCD8
            parada = local_player + 4
            endereço_da_parada = processo.read_int(parada)
            if keyboard.is_pressed('v'):
                if endereço_da_parada == 263:
                    processo.write_int(force_jump, 6)
                    sleep(0.01)
                    processo.write_int(force_jump, 4)
        janela.after(1, auto_bhop_agachado)


    def grenadepreview():
        if switch_do_grenadepreview.get() == 1:
            processo.write_int(endereço_base + 0xE06C38, valor_do_endereço_do_grenadepreview + 1)
        else:
            processo.write_int(endereço_base + 0xE06C38, valor_do_endereço_do_grenadepreview)


    def glow_guns():
        if switch_do_glow_on_guns.get() == 1:
            processo.write_int(endereço_base + 0xDFD4D8, valor_do_endereço_do_glow_das_armas_no_chão + 1)
        else:
            processo.write_int(endereço_base + 0xDFD4D8, valor_do_endereço_do_glow_das_armas_no_chão)


    tabview = ctk.CTkTabview(janela, width=250, height=170)
    tabview.pack()
    tabview.add('Visual')
    tabview.add('Auto Bhop')
    switch_do_wallhack = ctk.CTkSwitch(tabview.tab('Visual'), text='Wallhack', command=wallhack)
    switch_do_wallhack.place(x=4, y=5)
    switch_do_grenadepreview = ctk.CTkSwitch(tabview.tab('Visual'), text='Grenade Preview', command=grenadepreview)
    switch_do_grenadepreview.place(x=4, y=42)
    switch_do_glow_on_guns = ctk.CTkSwitch(tabview.tab('Visual'), text='Glow on Guns', command=glow_guns)
    switch_do_glow_on_guns.place(x=4, y=80)
    switch_do_auto_bhop_normal = ctk.CTkSwitch(tabview.tab('Auto Bhop'), text='Auto Bhop Normal', command=auto_bhop_normal)
    switch_do_auto_bhop_normal.place(x=4, y=5)
    switch_do_auto_bhop_agachado = ctk.CTkSwitch(tabview.tab('Auto Bhop'), text='Auto Bhop Agachado', command=auto_bhop_agachado)
    switch_do_auto_bhop_agachado.place(x=4, y=42)
    made_by = ctk.CTkLabel(janela, text=' Made by: Tiago.').place(x=7, y=184)
    meu_website = ctk.CTkLabel(janela, text='My website:').place(x=188, y=184)
    link_do_meu_website = ctk.CTkButton(janela, text=' https://tiago.fun/', width=0, height=0, command=abrir_link).place(x=260, y=187)
    janela.mainloop()
    sleep(0.01)
    processo.write_int(endereço_base + 0xDE5670, valor_do_endereço_do_wallhack)
    sleep(0.01)
    processo.write_int(endereço_base + 0xE06C38, valor_do_endereço_do_grenadepreview)
    sleep(0.01)
    processo.write_int(endereço_base + 0xDFD4D8, valor_do_endereço_do_glow_das_armas_no_chão)
else:
    jogo_não_encontrado = ctk.CTk()
    jogo_não_encontrado.title('Jogo não Encontrado')
    jogo_não_encontrado.geometry('650x120')
    jogo_não_encontrado.resizable(width=False, height=False)


    def ok():
        jogo_não_encontrado.destroy()


    aviso2 = ctk.CTkLabel(jogo_não_encontrado, text='⚠️' + 'AVISO' + '⚠️')
    aviso2.pack()
    processo_não_encontrado = ctk.CTkLabel(jogo_não_encontrado, text='O jogo Counter-Strike Global Offensive não foi encontrado. Tente Novamente.')
    processo_não_encontrado.pack()
    observação_sobre_a_janela = ctk.CTkLabel(jogo_não_encontrado, text='Está janela sempre vai aparecer quando o jogo Counter-Strike Global Offensive não estiver em execução.')
    observação_sobre_a_janela.pack()
    botão_ok = ctk.CTkButton(jogo_não_encontrado, text='OK', command=ok)
    botão_ok.pack()
    jogo_não_encontrado.mainloop()
