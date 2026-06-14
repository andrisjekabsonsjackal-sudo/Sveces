# Cenu zīmju ģenerators (English Version for GBS St Georges House)
# Saglabā šo kā generate_tags.py tajā pašā mapē, kur atrodas logo.png

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Amber and Flames - Price Tags</title>
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background-color: #fff;
        }
        /* Režģis izkārtojumam */
        .grid { 
            display: flex; 
            flex-wrap: wrap; 
            gap: 20px; 
            justify-content: flex-start; 
            padding: 20px; 
        }
        /* Kartiņas dizains */
        .tag {
            border: 2px dashed #b85e00;
            width: 180px;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            background-color: #fafafa;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .logo { 
            width: 110px; 
            height: auto; 
            margin-bottom: 12px; 
        }
        .title { 
            font-size: 16px; 
            font-weight: 600; 
            color: #2c3e50; 
            margin-bottom: 10px; 
            min-height: 45px; 
            line-height: 1.2;
        }
        .price { 
            font-size: 26px; 
            color: #b85e00; 
            font-weight: bold; 
            margin-bottom: 10px;
        }
        .footer {
            font-size: 9px;
            color: #7f8c8d;
            text-transform: uppercase;
            letter-spacing: 1px;
            border-top: 1px solid #ddd;
            padding-top: 8px;
            width: 80%;
        }
        
        /* Drukāšanas iestatījumi */
        @media print {
            body { -webkit-print-color-adjust: exact; }
            .tag { page-break-inside: avoid; }
        }
    </style>
</head>
<body>
    <div class="grid">
"""

# Produktu saraksts (viss angliski un pielāgots GBS auditorijai)
products = [
    {"name": "Frog & Flower Decorative Candle", "price": "£4.00"},
    {"name": "Moon & Clouds Glass Candle", "price": "£3.00"},
    {"name": "Classic Red Glass Candle", "price": "£2.50"},
    {"name": "Sculptural Figure Gift Set", "price": "£5.00"},
    
    # Dublikāti, lai uzreiz izdrukājas vairākas zīmes, ko sagriezt
    {"name": "Frog & Flower Decorative Candle", "price": "£4.00"},
    {"name": "Moon & Clouds Glass Candle", "price": "£3.00"},
    {"name": "Classic Red Glass Candle", "price": "£2.50"},
    {"name": "Sculptural Figure Gift Set", "price": "£5.00"},
]

# Ģenerējam HTML katram produktam
for item in products:
    html_content += f"""
        <div class="tag">
            <img src="logo.png" class="logo" alt="Amber and Flames">
            <div class="title">{item['name']}</div>
            <div class="price">{item['price']}</div>
            <div class="footer">Handcrafted in Leeds</div>
        </div>
    """

html_content += """
    </div>
</body>
</html>
"""

with open("price_tags.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("English price tags generated successfully! Open 'price_tags.html' to print.")