from sharepoint import SharePoint
import os

# Configurações
folder_name = 'TV'  # Nome da pasta no SharePoint
output_folder = "images"  # Pasta para salvar as imagens localmente

# Criar a pasta se não existir
os.makedirs(output_folder, exist_ok=True)

# Instancia a classe SharePoint
sp = SharePoint()

# Lista todos os arquivos na pasta especificada
files = sp.list_files(folder_name)

# Lista para armazenar as tags de imagens para o HTML
image_tags = []

# Itera sobre os arquivos e baixa apenas imagens
for file_name in files:
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        print(f"Downloading {file_name}...")
        
        # Baixar o arquivo
        file_content = sp.download_file(file_name, folder_name)

        # Salvar o arquivo localmente
        image_path = os.path.join(output_folder, file_name)
        with open(image_path, 'wb') as f:
            f.write(file_content)
        print(f"{file_name} downloaded successfully.")
        
        # Adiciona a tag img ao HTML
        image_tag = f'<img class="mySlides" src="{output_folder}/{file_name}" alt="{file_name.split(".")[0]}">'
        image_tags.append(image_tag)

print("All images downloaded and saved.")

# Construir o HTML dinamicamente
html_content = f"""
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="refresh" content="1800" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Indicadores GC - Slideshow</title>
        <link rel="shortcut icon" href="favicon.png"> 
        <style>
            * {{
                box-sizing: border-box;
            }}
            body {{
                font-family: Verdana, sans-serif;
                height: 100%;
                overflow: hidden;
                background-color: #FFFFFF;
            }}
            .mySlides {{
                display: none;
            }}
            img {{
                vertical-align: middle;
                width: 100%;
                height: 95vh; /* Aumenta a altura para quase ocupar toda a tela */
            }}
            .slideshow-container {{  
                max-width: 100%;
                width: 100%;
                height: 100%;
                position: relative;
                margin: auto;
                margin-top: -12px;
            }}
        </style>
    </head>
    <body>
        <div class="slideshow-container">
            {''.join(image_tags)}
        </div>

        <script>
            var slideIndex = 0;
            showSlides();

            function showSlides() {{    
                var i;    
                var slides = document.getElementsByClassName("mySlides"); 

                for (i = 0; i < slides.length; i++) {{
                    slides[i].style.display = "none";    
                }}    

                if (slideIndex >= slides.length) {{
                    slideIndex = 0;
                }}    

                slides[slideIndex].style.display = "block";

                setTimeout(showSlides, 20000); /* Tempo de exibição por slide (20 segundos) */
                slideIndex++; 
            }}
        </script>
    </body>
</html>
"""

# Salvar o HTML em um arquivo
html_file_path = "index.html"
with open(html_file_path, "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

print(f"HTML file generated: {html_file_path}")
