import re
import UIElements as UIE
import ipCalClass as ip

ip_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
ip_pattern = re.compile(ip_regex)

class IPManager:

    #Metodo confirmar exit
    @staticmethod
    def yes_click(e,page):
        page.window_destroy()

    #Metodo confirmar seguir
    @staticmethod
    def no_click(e,page):
        UIE.UIElements.confirm_dialog.open = False
        page.update()
    
    #Metodo dialogo exit
    @staticmethod
    def window_event(e,page):
        if e.data == "close":
            page.dialog = UIE.UIElements.confirm_dialog
            UIE.UIElements.confirm_dialog.open = True
            page.update()

    #Metodo limpiar campos
    @staticmethod
    def btn_clear_click(e,page):
        UIE.UIElements.ip_txtField.value=None
        UIE.UIElements.sub_dropdown.value=None
        page.update()

    #Metodo validar ip en campo
    @staticmethod
    def validate_ip(ip_value):
        return ip_pattern.match(ip_value)

    #Metodo invalidar ip
    @staticmethod
    def handle_invalid_ip(page):
        UIE.UIElements.ip_txtField.error_text = 'IP inválida'
        page.update()

    #Metodo invalidar dropdown
    @staticmethod
    def handle_missing_sub_prefix(page):
        UIE.UIElements.sub_dropdown.error_text = "Selecciona un subfijo"
        page.update()

    #Metodo calcular IP
    @staticmethod
    def btn_calcular_click(e, page):
        ip_value = UIE.UIElements.ip_txtField.value
        sub_prefix_value = UIE.UIElements.sub_dropdown.value

        if ip_value and sub_prefix_value is not None:
            if IPManager.validate_ip(ip_value):
                try:
                    UIE.UIElements.ip_txtField.error_text = None
                    UIE.UIElements.sub_dropdown.error_text = None
                    page.update()
                    
                    ip_addr = f"{ip_value}/{sub_prefix_value}"
                    ipAddress = ip.ipCalClass(ip_addr)
                    ipAddress.imp_infor(ip_addr)
                    page.go('/Tabla')
                
                except (IndexError, ValueError):
                    page.error("ERROR 404")
            else:
                IPManager.handle_invalid_ip(page)
        else:
            if not IPManager.validate_ip(ip_value):
                IPManager.handle_invalid_ip(page)
            else:
                UIE.UIElements.ip_txtField.error_text = None
                page.update()
            if sub_prefix_value is None:
                IPManager.handle_missing_sub_prefix(page)
            else:
                UIE.UIElements.sub_dropdown.error_text = None
                page.update()

    #Metodo events
    def events(page):
        page.on_window_event = lambda e: IPManager.window_event(e,page)
        UIE.UIElements.btn_confirm.on_click = lambda e: IPManager.yes_click(e,page)
        UIE.UIElements.btn_deny.on_click = lambda e: IPManager.no_click(e,page)
        UIE.UIElements.btn_calcular.on_click = lambda e: IPManager.btn_calcular_click(e,page)
        UIE.UIElements.btn_clear_txtf.on_click = lambda e: IPManager.btn_clear_click(e,page)