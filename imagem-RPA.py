from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests
from io import BytesIO


# abrir uma imagem
img = Image.open("gremio.webp")
img.show()
# Redirecionar a imagem para 200x200 pixels
img_resized = img.resize((100, 100))

# Salvar a iamgem redimensionada
img_resized.save('imagem_redimensionada.webp')
img_resized.show()


img = Image.open('gremio.webp') # abre a imagem normal
img_blur = img.filter(ImageFilter.BLUR) # desfoca a iamgem
img_blur.save('imagem_desfocada.webp') # salva a imagem desfocada
img_blur.show() # mostra a imagem desfocada


img = Image.open('gremio.webp')
img.convert('RGB').save('imagem_convertida.png', 'PNG') # coverte a imagem de webp para png <3
img.show()






# Função para editar a imagem
def editar_imagem(caminho_imagem, texto, novo_tamanho, filtro):
    # Abrir a imagem
    img = Image.open(caminho_imagem)

    # Redimensionar
    img = img.resize(novo_tamanho)

    # Aplicar filtro
    if filtro == "blur":
        img = img.filter(ImageFilter.BLUR)
    elif filtro == "contour":
        img = img.filter(ImageFilter.CONTOUR)
    elif filtro == "sharpen":
        img = img.filter(ImageFilter.SHARPEN)

    # Adicionar texto
    draw = ImageDraw.Draw(img)
    fonte = ImageFont.load_default()
    draw.text((100, 100), texto, fill="white", font=fonte)
    draw.size(50)

    # Salvar a imagem
    img.save("imagem_editada.jpg")
    print("Imagem editada salva como 'imagem_editada.jpg'")

# MAIN
# Exemplo de uso
editar_imagem("gremio.webp", "Olá, Mundo!", (800, 600), "sharpen") # passa os valores em ordem para caminho_imagem, texto add a imagem, tamanho redirecionado, e o filtro


def text_in_image_with_api():
    url_api = "https://cataas.com/cat"
    try: 
       response = requests.get(url_api) # faz a requisição da api por meio de sua url
       response.raise_for_status() # verifica se a requisição foi bem-sucedida
       return Image.open(BytesIO(response.content)) 
    
    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None    
    
imagem = text_in_image_with_api("https://cataas.com/cat")
imagem.save('cat.png')

text_in_image_with_api()




