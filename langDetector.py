import tkinter as tk
from tkinter import messagebox
from langdetect import detect, DetectorFactory

# Evita que los resultados varien en otras ejecuciones
DetectorFactory.seed = 0


# Funcion que toma texto como parametro y regresa el idioma detectado
def detect_language(text):
    try:
        return detect(text)
    except Exception as e:
        return None


# Funccion que se activa con el boton para menejar la deteccion del texto
def on_detect_button_click():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        code = detect_language(text)
        if code:
            messagebox.showinfo("Resultado", f"El idioma detectado es: {code}")
        else:
            messagebox.showerror("Error", "No se pudo detectar el idioma.")
    else:
        messagebox.showwarning("Por favor, ingrese un texto.")


def main():
    window = tk.Tk()
    window.title("Detector de Idioma")

    global text_entry
    text_label = tk.Label(window, text="Ingrese el texto:")
    text_label.pack(pady=10)

    text_entry = tk.Text(window, height=10, width=50)
    text_entry.pack(pady=5)

    detect_button = tk.Button(
        window, text="Detectar Idioma", command=on_detect_button_click
    )
    detect_button.pack(pady=20)

    window.mainloop()


if __name__ == "__main__":
    main()
