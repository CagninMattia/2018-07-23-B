import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        anno = self._view.txt_year.value
        xg = self._view.txt_xg.value
        if anno is not None and xg is not None:
            self._view.txt_result.controls.clear()
            self._view.update_page()
            try:
                anno = int(anno)
                xg = int(xg)
            except ValueError:
                self._view.txt_result.controls.clear()
                self._view.create_alert("Inserisci un numero intero. ")
                self._view.update_page()
                return
            if 1906 <= anno <= 2014:
                if 1 <= xg <= 180:
                    self._model.crea_grafo(anno, xg)
                    num_nodi = self._model.num_nodi()
                    num_archi = self._model.num_archi()
                    self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {num_nodi}"))
                    self._view.txt_result.controls.append(ft.Text(f"Numero archi: {num_archi}"))
                    nodi = self._model.get_peso_nodi()
                    for c, v in nodi.items():
                        self._view.txt_result.controls.append(ft.Text(f"Nodo {c.id}, somma pesi su archi = {v}"))
                    self._view.txt_t1.disabled = False
                    self._view.txt_alfa.disabled = False
                    self._view.btn_simula.disabled = False
                    self._view.update_page()
                else:
                    self._view.create_alert("xG deve essere tra 1 e 180.")
                    self._view.update_page()
            else:
                self._view.create_alert("anno deve essere tra 1906 e 2014.")
                self._view.update_page()
        else:
            self._view.txt_result.controls.clear()
            self._view.create_alert("Selezionare tutti e due i campi. ")
            self._view.update_page()

    def handle_path(self, e):
        pass
