from django.shortcuts import render

# Create your views here.
def index (request):
    context = {
        'title': 'index',
    }
    return render(request,'mainapp/index.html', context )

def products (request):
    context = {
        'title': 'products',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00, 'src':'vendor/img/products/Adidas-hoodie.png', 'card_text' : 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00, 'src':'vendor/img/products/Blue-jacket-The-North-Face.png', 'card_text' : 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00,'src':'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png', 'card_text' : 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00, 'src':'vendor/img/products/Black-Dr-Martens-shoes.png', 'card_text' : 'Гладкий кожаный верх. Натуральный материал.'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590.00, 'src':'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png', 'card_text' : 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890.00, 'src':'vendor/img/products/Adidas-hoodie.png', 'card_text' : 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
        ]
    }
    return render(request,'mainapp/products.html',context )
