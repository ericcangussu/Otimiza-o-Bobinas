import streamlit as st
import streamlit.components.v1 as components

# HTML e JavaScript para a exibição dos slides de Power BI
html_code = '''
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="refresh" content="1800" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
    
        <title>Indicadores GC - Power Portal</title>
        <link rel="shortcut icon" HREF="https://www.powerportal.com.br/img/favicon.png"> 
        <style>
            * {
                box-sizing: border-box;
            }
            body {
                font-family: Verdana, sans-serif;
                height: 100%;
                overflow:hidden;
                background-color: #FFFFFF;
            }
            .mySlides {
                display: none;
            }
            iframe {
                vertical-align: center;
                width: 100%;
                height: 100vh;
            }
            .slideshow-container {  
                max-width: 1000%;
                width: 100%;
                height: 100%;
                position: relative;
                margin: auto;
                margin-top: -12px;
            }
            .text {  
                color: #f2f2f2;
                font-size: 15px;
                padding: 8px 12px;
                position: absolute;
                bottom: 8px;
                height: 100%; 
                width: 100%;
                text-align: center;
            }
            .numbertext {
                color: #f2f2f2; 
                font-size: 12px; 
                padding: 8px 12px; 
                position: absolute; 
                top: 0;
            }
            .dot { 
                height: 15px; 
                width: 15px; 
                margin: 0 2px; 
                background-color: #bbb; 
                border-radius: 50%; 
                display: inline-block; 
                transition: background-color 0.6s ease;
            }
            .active {  
                background-color: #717171; 
                height: 100%;
            }

            .fade { 
                -webkit-animation-name: fade; 
                -webkit-animation-duration: 0.2s; 
                animation-name: fade; 
                animation-duration: 0.2s;
            }
            @-webkit-keyframes fade {  
                from {
                   opacity: .4;
                } 
                to {
                   opacity: 1;
                }
            }
            @keyframes fade { 
                from {
                   opacity: .4;
                } 
                to {
                   opacity: 1;
                }
            }

            .ajuste{ 
                margin-top:-5;
                margin-left:-8px;
                width: 101% !important;
                height: 109vh !important;
            }
        </style>
    </head>
    <body>
        <div class="slideshow-container ajuste">
            <iframe class="mySlides nenhum ajuste" src="https://app.powerbi.com/view?r=eyJrIjoiY2U5OGVmZDItMjNiYy00ZThjLWIwNTktZjMwNzc5OGIwY2JkIiwidCI6IjZkOWMyYzg0LTRkMjQtNDc3MC04MWE5LTdjZjg0ZmEyNDMwZCJ9&pageName=ReportSection1dc50c032a19a26803b4" frameborder="0" allowFullScreen="true"></iframe>
        
            <iframe class="mySlides nenhum ajuste" src="https://app.powerbi.com/view?r=eyJrIjoiY2U5OGVmZDItMjNiYy00ZThjLWIwNTktZjMwNzc5OGIwY2JkIiwidCI6IjZkOWMyYzg0LTRkMjQtNDc3MC04MWE5LTdjZjg0ZmEyNDMwZCJ9&pageName=ReportSectione3cd9c1c09aa9410039d" frameborder="0" allowFullScreen="true"></iframe>
        
            <iframe class="mySlides nenhum ajuste" src="https://app.powerbi.com/view?r=eyJrIjoiY2U5OGVmZDItMjNiYy00ZThjLWIwNTktZjMwNzc5OGIwY2JkIiwidCI6IjZkOWMyYzg0LTRkMjQtNDc3MC04MWE5LTdjZjg0ZmEyNDMwZCJ9&pageName=ReportSection105c4019e48dc52a7222" frameborder="0" allowFullScreen="true"></iframe>
        <br>
        </div>

        <script>
            var slideIndex = 0;

            showSlides();

            function showSlides() {    
                var i;    
                var slides = document.getElementsByClassName("mySlides"); 

                for (i = 0; i < slides.length; i++) {
                   slides[i].style.display = "none";    
                }    

                if (slideIndex >= slides.length) {
                   slideIndex = 0;
                }    

                slides[slideIndex].style.display = "block";

                setTimeout(showSlides, 20000);
                slideIndex++; 
            }
        </script>
    </body>
</html>
'''

# Renderiza o código HTML no Streamlit
components.html(html_code, height=800)
