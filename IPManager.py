import re
import UIElements as UIE
import ipCalClass as ip

# Expresión regular para validar direcciones IP
ip_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
ip_pattern = re.compile(ip_regex)

class IPManager:

    # Método para manejar el evento de hacer clic en "Sí" para salir
    @staticmethod
    def yes_click(e,page):
        page.window_destroy()

    # Método para manejar el evento de hacer clic en "No" para seguir
    @staticmethod
    def no_click(e,page):
        UIE.UIElements.confirm_dialog.open = False
        page.update()
    
    # Método para manejar eventos de la ventana (cierre)
    @staticmethod
    def window_event(e,page):
        if e.data == "close":
            page.dialog = UIE.UIElements.confirm_dialog
            UIE.UIElements.confirm_dialog.open = True
            page.update()

    #Metodo para limpiar campos
    @staticmethod
    def btn_clear_click(e,page):
        UIE.UIElements.ip_txtField.value=None
        UIE.UIElements.sub_dropdown.value=None
        #UIE.UIElements.sub2_dropdown.value=None
        page.update()

    # Método para validar una dirección IP ingresada
    @staticmethod
    def validate_ip(input_ip_addr):
        return ip_pattern.match(input_ip_addr)

    # Método para manejar una IP inválida
    @staticmethod
    def handle_invalid_ip(page):
        UIE.UIElements.ip_txtField.error_text = 'IP inválida'
        page.update()

    # Método para manejar un subfijo faltante
    @staticmethod
    def handle_missing_sub_prefix(page):
        UIE.UIElements.sub_dropdown.error_text = "Selecciona un subfijo"
        page.update()

    # Método para manejar el evento de hacer clic en "Calcular"
    @staticmethod
    def btn_calcular_click(e, page):
        input_ip_addr = UIE.UIElements.ip_txtField.value
        sub_prefix_value = UIE.UIElements.sub_dropdown.value

        if input_ip_addr and sub_prefix_value is not None:
            if IPManager.validate_ip(input_ip_addr):
                try:
                    UIE.UIElements.ip_txtField.error_text = None
                    UIE.UIElements.sub_dropdown.error_text = None
                    page.update()
                    
                    ip_addr = f"{input_ip_addr}/{sub_prefix_value}"
                    ipAddress = ip.ipCalClass(ip_addr)
                    ipAddress.imp_infor(ip_addr)
                    page.go('/Tabla')
                
                except (IndexError, ValueError):
                    page.error("ERROR 404")
            else:
                IPManager.handle_invalid_ip(page)
        else:
            if not IPManager.validate_ip(input_ip_addr):
                IPManager.handle_invalid_ip(page)
            else:
                UIE.UIElements.ip_txtField.error_text = None
                page.update()
            if sub_prefix_value is None:
                IPManager.handle_missing_sub_prefix(page)
            else:
                UIE.UIElements.sub_dropdown.error_text = None
                page.update()

    # Método para asignar eventos a elementos UI
    def events(page):
        page.on_window_event = lambda e: IPManager.window_event(e,page)
        UIE.UIElements.btn_confirm.on_click = lambda e: IPManager.yes_click(e,page)
        UIE.UIElements.btn_deny.on_click = lambda e: IPManager.no_click(e,page)
        UIE.UIElements.btn_calcular.on_click = lambda e: IPManager.btn_calcular_click(e,page)
        UIE.UIElements.btn_clear_txtf.on_click = lambda e: IPManager.btn_clear_click(e,page)