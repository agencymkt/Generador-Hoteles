#!/usr/bin/env python
# Este archivo usa el encoding: utf-8

def image_tour_gallery(
    section_name,
    hotel_name,
    image_structure,
    link_tour,
    link_gallery,
    text_gallery,
    content, 
    has_toggle
):

    if has_toggle:
        no_of_lines = int(input("Número de líneas: "))
        lines = []
        for i in range(no_of_lines):
            line = input()
            lines.append(line + "<br>")
        text = '\n'.join(lines)  

        section_code = """<div class="tab-content">
                <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; z-index: 31; margin-bottom: 10px;">""" + section_name + """ (360º)</h3>
                <div class="tab-img">
                """ + image_structure + """
                <div class="elementor-element elementor-element-cd405a9 elementor-widget elementor-widget-button" data-id="cd405a9" data-element_type="widget" data-widget_type="button.default">
                <div class="elementor-widget-container">
                <div class="elementor-button-wrapper"><a id="button-tour" class="elementor-button-link elementor-button elementor-size-sm" role="button" """ + link_tour + """>
                <span class="elementor-button-content-wrapper">
                <span class="elementor-button-icon elementor-align-icon-left">
                <i class="far fa-play-circle" aria-hidden="true"></i> </span>
                <span class="elementor-button-text">Ver tour virtual en 360º</span>
                </span>
                </a></div>
                </div>
                </div>
                <div id="div-carousel" class="elementor-element elementor-element-fe9b671 elementor-widget elementor-widget-button" data-id="fe9b671" data-element_type="widget" data-widget_type="button.default">
                <div class="elementor-widget-container">
                <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" role="button" """ + link_gallery + """>
                <span class="elementor-button-content-wrapper">
                <span class="elementor-button-icon elementor-align-icon-left">
                <i class="far fa-eye" aria-hidden="true"></i> </span>
                <span class="elementor-button-text">Ver más fotos de""" + text_gallery + """</span>
                </span>
                </a></div>
                </div>
                </div>
                """ + content + """
                <button class="collapsible" type="button">Horarios y Servicios</button>
                <div class="content">
                """ + text + """
                </div>
                </div>
                </div>
            """
    else:    
        section_code = """<div class="tab-content">
                    <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; z-index: 31; margin-bottom: 10px;">""" + section_name + """ (360º)</h3>
                    <div class="tab-img">
                    """ + image_structure + """
                    <div class="elementor-element elementor-element-cd405a9 elementor-widget elementor-widget-button" data-id="cd405a9" data-element_type="widget" data-widget_type="button.default">
                    <div class="elementor-widget-container">
                    <div class="elementor-button-wrapper"><a id="button-tour" class="elementor-button-link elementor-button elementor-size-sm" role="button" """ + link_tour + """>
                    <span class="elementor-button-content-wrapper">
                    <span class="elementor-button-icon elementor-align-icon-left">
                    <i class="far fa-play-circle" aria-hidden="true"></i> </span>
                    <span class="elementor-button-text">Ver tour virtual en 360º</span>
                    </span>
                    </a></div>
                    </div>
                    </div>
                    <div id="div-carousel" class="elementor-element elementor-element-fe9b671 elementor-widget elementor-widget-button" data-id="fe9b671" data-element_type="widget" data-widget_type="button.default">
                    <div class="elementor-widget-container">
                    <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" role="button" """ + link_gallery + """>
                    <span class="elementor-button-content-wrapper">
                    <span class="elementor-button-icon elementor-align-icon-left">
                    <i class="far fa-eye" aria-hidden="true"></i> </span>
                    <span class="elementor-button-text">Ver más fotos de""" + text_gallery + """</span>
                    </span>
                    </a></div>
                    </div>
                    </div>
                    """ + content + """
                    </div>
                    </div>
                """
    hs = open(section_name + " - " + hotel_name + ".html", 'w')
    hs.write(section_code)

    print(section_code)


def image_tour(
    section_name,
    hotel_name,
    image_structure,
    link_tour,
    content,
    has_toggle
):

    if has_toggle:
        no_of_lines = int(input("Número de líneas: "))
        lines = []
        for i in range(no_of_lines):
            line = input()
            lines.append(line + "<br>")
        text = '\n'.join(lines)   

        section_code = """<div class="tab-content">
                <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; z-index: 31; margin-bottom: 10px;">""" + section_name + """ (360º)</h3>
                <div class="tab-img">
                """ + image_structure + """
                <div class="elementor-element elementor-element-cd405a9 elementor-widget elementor-widget-button" data-id="cd405a9" data-element_type="widget" data-widget_type="button.default">
                <div class="elementor-widget-container">
                <div class="elementor-button-wrapper"><a id="button-tour" class="elementor-button-link elementor-button elementor-size-sm" role="button" """ + link_tour + """>
                <span class="elementor-button-content-wrapper">
                <span class="elementor-button-icon elementor-align-icon-left">
                <i class="far fa-play-circle" aria-hidden="true"></i> </span>
                <span class="elementor-button-text">Ver tour virtual en 360º</span>
                </span>
                </a></div>
                </div>
                </div>
                """ + content + """
                <button class="collapsible" type="button">Horarios y Servicios</button>
                <div class="content">
                """ + text + """
                </div>
                </div>
                </div>
            """
    else:
        section_code = """<div class="tab-content">
                    <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; z-index: 31; margin-bottom: 10px;">""" + section_name + """ (360º)</h3>
                    <div class="tab-img">
                    """ + image_structure + """
                    <div class="elementor-element elementor-element-cd405a9 elementor-widget elementor-widget-button" data-id="cd405a9" data-element_type="widget" data-widget_type="button.default">
                    <div class="elementor-widget-container">
                    <div class="elementor-button-wrapper"><a id="button-tour" class="elementor-button-link elementor-button elementor-size-sm" role="button" """ + link_tour + """>
                    <span class="elementor-button-content-wrapper">
                    <span class="elementor-button-icon elementor-align-icon-left">
                    <i class="far fa-play-circle" aria-hidden="true"></i> </span>
                    <span class="elementor-button-text">Ver tour virtual en 360º</span>
                    </span>
                    </a></div>
                    </div>
                    </div>
                    """ + content + """
                    </div>
                    </div>
                """
    hs = open(section_name + " - " + hotel_name + ".html", 'w')
    hs.write(section_code)

    print(section_code)

def image_gallery(
    section_name,
    hotel_name,
    image_structure,
    link_gallery,
    text_gallery,
    content,
    has_toggle
):
    if has_toggle:
        no_of_lines = int(input("Número de líneas: "))
        lines = []
        for i in range(no_of_lines):
            line = input()
            lines.append(line + "<br>")
        text = '\n'.join(lines)  

        section_code = """<div class="tab-content">
                <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; z-index: 31; margin-bottom: 10px;">""" + section_name + """</h3>
                <div class="tab-img">
                """ + image_structure + """
                <div id="div-carousel" class="elementor-element elementor-element-fe9b671 elementor-widget elementor-widget-button" data-id="fe9b671" data-element_type="widget" data-widget_type="button.default">
                <div class="elementor-widget-container">
                <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" role="button" """ + link_gallery + """>
                <span class="elementor-button-content-wrapper">
                <span class="elementor-button-icon elementor-align-icon-left">
                <i class="far fa-eye" aria-hidden="true"></i> </span>
                <span class="elementor-button-text">Ver más fotos de""" + text_gallery + """</span>
                </span>
                </a></div>
                </div>
                </div>
                """ + content + """
                <button class="collapsible" type="button">Horarios y Servicios</button>
                <div class="content">
                """ + text + """
                </div>
                </div>
                </div>
            """
    else:
        section_code = """<div class="tab-content">
                    <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; z-index: 31; margin-bottom: 10px;">""" + section_name + """</h3>
                    <div class="tab-img">
                    """ + image_structure + """
                    <div id="div-carousel" class="elementor-element elementor-element-fe9b671 elementor-widget elementor-widget-button" data-id="fe9b671" data-element_type="widget" data-widget_type="button.default">
                    <div class="elementor-widget-container">
                    <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" role="button" """ + link_gallery + """>
                    <span class="elementor-button-content-wrapper">
                    <span class="elementor-button-icon elementor-align-icon-left">
                    <i class="far fa-eye" aria-hidden="true"></i> </span>
                    <span class="elementor-button-text">Ver más fotos de""" + text_gallery + """</span>
                    </span>
                    </a></div>
                    </div>
                    </div>
                    """ + content + """
                    </div>
                    </div>
                """
    hs = open(section_name + " - " + hotel_name + ".html", 'w')
    hs.write(section_code)

    print(section_code)

def image(
    section_name,
    hotel_name,
    image_structure,
    content,
    has_toggle
):

    if has_toggle:
        no_of_lines = int(input("Número de líneas: "))
        lines = []
        for i in range(no_of_lines):
            line = input()
            lines.append(line + "<br>")
        text = '\n'.join(lines)    

        section_code = """<div class="tab-content">
                <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; z-index: 31; margin-bottom: 10px;">""" + section_name + """ </h3>
                <div class="tab-img">
                """ + image_structure + """
                
                """ + content + """
                <button class="collapsible" type="button">Horarios y Servicios</button>
                <div class="content">
                """ + text + """
                </div>
                </div>
                </div>
            """
    else:
        section_code = """<div class="tab-content">
                    <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; z-index: 31; margin-bottom: 10px;">""" + section_name + """</h3>
                    <div class="tab-img">
                    """ + image_structure + """
                    
                    """ + content + """
                    
                    </div>
                    </div>
                """
    hs = open(section_name + " - " + hotel_name + ".html", 'w')
    hs.write(section_code)

    print(section_code)    

def only_content(
    section_name,
    hotel_name,
    content,
    has_toggle
):

    if has_toggle:
        no_of_lines = int(input("Número de líneas: "))
        lines = []
        for i in range(no_of_lines):
            line = input()
            lines.append(line + "<br>")
        text = '\n'.join(lines)
        section_code = """<div class="tab-content">
                <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; z-index: 31; margin-bottom: 10px;">""" + section_name + """ </h3>
                <div class="tab-img">
                """ + content + """
                <button class="collapsible" type="button">Horarios y Servicios</button>
                <div class="content">
                """ + text + """
                </div>
                </div>
                </div>
            """
    else:
        section_code = """<div class="tab-content">
                <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; z-index: 31; margin-bottom: 10px;">""" + section_name + """ </h3>
                <div class="tab-img">
                """ + content + """
                </div>
                </div>
            """


    hs = open(section_name + " - " + hotel_name + ".html", 'w')
    hs.write(section_code)

    print(section_code)   

def bedroom(
    section_name,
    hotel_name,
    image_structure,
    link_tour,
    link_gallery,
    no_subsections
):
    lines = []
    for i in range(no_subsections):

        name_subsection = input("\nNombre de la subsección: ")
        if i!= 0:
            lines.append("<h4 style=\"font: 14px/29px Arial, serif; color: #292d34; font-weight: bold;\">—" + name_subsection + "</h4>")
        else:
            lines.append("<h4 style=\"font: 14px/29px Arial, serif; color: #292d34; font-weight: bold; margin-top: -15px;\">—" + name_subsection + "</h4>")

        no_of_lines = int(input("\nNúmero de párrafos de la subsección: "))
        for j in range(no_of_lines):
            line = input()
            lines.append("<p>" + line + "</p>")

    content = '\n'.join(lines)

    section_code = """<div class="row">

    <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; margin-bottom: 10px;">""" + section_name + """</h3>
    
    <div class="column1">
    
    """ + image_structure + """
    <div class="elementor-element elementor-element-b909e2d elementor-widget elementor-widget-button" data-id="b909e2d" data-element_type="widget" data-widget_type="button.default">
    <div class="elementor-widget-container">
    <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" style="text-align: left;" role="button" """ + link_tour + """>
    <span class="elementor-button-content-wrapper">
    <span class="elementor-button-icon elementor-align-icon-left">
    <i class="far fa-play-circle" aria-hidden="true"></i> </span>
    <span class="elementor-button-text">Ver tour virtual 360º</span>
    </span>
    </a></div>
    </div>
    </div>

    <div id="div-carousel" class="elementor-element elementor-element-94af6b5 elementor-widget elementor-widget-button" data-id="94af6b5" data-element_type="widget" data-widget_type="button.default">
    <div class="elementor-widget-container">
    <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" style="text-align: left;" role="button" """ + link_gallery + """>
    <span class="elementor-button-content-wrapper">
    <span class="elementor-button-icon elementor-align-icon-left">
    <i class="far fa-eye" aria-hidden="true"></i> </span>
    <span class="elementor-button-text">Ver más fotos de la Habitación</span>
    </span>
    </a></div>
    </div>
    </div>
    </div>

    <div class="column2">

    """ + content + """

    </div>
    </div>
    """
    hs = open(section_name + " - " + hotel_name + ".html", 'w')
    hs.write(section_code)

    print(section_code)   

def restaurants(
    section_name,
    hotel_name,
    image_structure,
    content,
    no_subsections
):
    lines = []
    for i in range(no_subsections):

        name_subsection = input("\nNombre del restaurante: ")
        country = input("Tipo de comida: ")
        service = input("Tipo de servicio: ")

        if i == 0:
            lines.append(""" <h4 id="restaurante-1" style="display: block; font: 17px/29px Arial, serif; color: #292d34; font-weight: bold;">""" + name_subsection + """</h4>
                        <div class="etiqueta"><i class="fas fa-utensils" style="margin-right: 5px;" aria-hidden="true"></i>""" + country + """</div>
                        <div class="etiqueta"><i class="fas fa-concierge-bell" style="margin-right: 5px;" aria-hidden="true"></i>""" + service + """</div>""")
        else:
            lines.append(""" <h4 style="display: block; font: 17px/29px Arial, serif; color: #292d34; font-weight: bold;">""" + name_subsection + """</h4>
                        <div class="etiqueta"><i class="fas fa-utensils" style="margin-right: 5px;" aria-hidden="true"></i>""" + country + """</div>
                        <div class="etiqueta"><i class="fas fa-concierge-bell" style="margin-right: 5px;" aria-hidden="true"></i>""" + service + """</div>""")

        image_parts = []
        print("Código de imagen: ")
        for k in range(5):
            image_parts.append(input())
        image = '\n'.join(image_parts)
        lines.append(image)

        tour = input("Url del popup con tour (Inserte N si no hay tour): \n")
        if tour!="n" and tour!="N":
            lines.append("""<div class="elementor-element elementor-element-b909e2d elementor-widget elementor-widget-button" data-id="b909e2d" data-element_type="widget" data-widget_type="button.default">
                        <div class="elementor-widget-container">
                        <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" style="text-align: left;" role="button" """ + tour + """>
                        <span class="elementor-button-content-wrapper">
                        <span class="elementor-button-icon elementor-align-icon-left">
                        <i class="far fa-play-circle" aria-hidden="true"></i> </span>
                        <span class="elementor-button-text">Ver tour virtual 360º</span>
                        </span>
                        </a></div>
                        </div>
                        </div>""")


        gallery = input("Url del popup con la galería (Inserte N si no hay galería): \n")
        if gallery!="n" and gallery!="N":
            lines.append("""<div id="div-carousel" class="elementor-element elementor-element-94af6b5 elementor-widget elementor-widget-button" data-id="94af6b5" data-element_type="widget" data-widget_type="button.default">
                        <div class="elementor-widget-container">
                        <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" style="text-align: left;" role="button" """ + gallery + """>
                        <span class="elementor-button-content-wrapper">
                        <span class="elementor-button-icon elementor-align-icon-left">
                        <i class="far fa-eye" aria-hidden="true"></i> </span>
                        <span class="elementor-button-text">Ver más fotos de """ + name_subsection + """</span>
                        </span>
                        </a></div>
                        </div>
                        </div>""")       

        no_of_lines = int(input("\nNúmero de párrafos de la subsección: "))
        for j in range(no_of_lines):
            line = input()
            if gallery == "N" and tour!="N" and j == 0:
                lines.append("<p style=\"padding-top: 7%;\">" + line + "</p>") 
            elif tour == "N" and gallery!="N" and j == 0:
                lines.append("<p style=\"padding-top: 7%;\">" + line + "</p>") 
            else:
                lines.append("<p>" + line + "</p>")

        no_of_toggle_lines = int(input("\nNúmero de párrafos del toggle: "))
        toggle_lines = []
        for k in range(no_of_toggle_lines):
            line = input()
            toggle_lines.append(line + "<br>")
        toggle_content = """<button class="collapsible" type="button">Horarios y Servicios</button>
                <div class="content">
                """ + '\n'.join(toggle_lines)+ """
                </div>"""
        lines.append(toggle_content)

    text = '\n'.join(lines)

    section_code = """<div class="tab-content">
    
    <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; margin-bottom: 10px;">""" + section_name + """ (360°)</h3>
    
    <div class="tab-img">

    """ + image_structure + """

    <div class="elementor-element elementor-element-715fc03 elementor-widget elementor-widget-button" data-id="715fc03" data-element_type="widget" data-widget_type="button.default">
    <div class="elementor-widget-container">
    <div class="elementor-button-wrapper"><a id="button-tour" class="elementor-button-link elementor-button elementor-size-sm" role="button" href="#restaurante-1">
    <span class="elementor-button-content-wrapper">
    <i class="far fa-play-circle" style="display: inline; font-size: 13px; margin-right: 5px;" aria-hidden="true"></i>
    <span class="elementor-button-text">Ver tour virtual en 360º
    <i class="fas fa-arrow-down" style="display: inline; font-size: 13px;"></i></span>
    </span></a></div>
    </div>
    </div>

    <div id="div-carousel" class="elementor-element elementor-element-ffa0974 elementor-widget elementor-widget-button" data-id="ffa0974" data-element_type="widget" data-widget_type="button.default">
    <div class="elementor-widget-container">
    <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" role="button" href="#restaurante-1">
    <span class="elementor-button-content-wrapper">
    <i class="far fa-eye" style="display: block-inline; font-size: 13px; margin-right: 5px;" aria-hidden="true"></i>
    <span class="elementor-button-text">Ver más fotos de Restaurantes
    <i class="fas fa-arrow-down" style="display: block-inline; font-size: 13px;"></i>
    </span>
    </span></a></div>
    </div>
    </div>

    """ + content + text + """

    </div>
    </div>
    """
    hs = open(section_name + " - " + hotel_name + ".html", 'w')
    hs.write(section_code)

    print(section_code)  
    
def with_subsections(
    section_name,
    hotel_name,
    image_structure,
    content,
    no_subsections
):
    lines = []
    for i in range(no_subsections):

        name_subsection = input("\nNombre del la subsección: ")

        if i == 0:
            lines.append(""" <h4 id=\"""" + section_name + """-1" style="display: block; font: 17px/29px Arial, serif; color: #292d34; font-weight: bold;">""" + name_subsection + """</h4>""")
        else:
            lines.append(""" <h4 style="display: block; font: 17px/29px Arial, serif; color: #292d34; font-weight: bold;">""" + name_subsection + """</h4>""")

        image_parts = []
        print("Código de imagen: ")
        for k in range(5):
            image_parts.append(input())
        image = '\n'.join(image_parts)
        lines.append(image)

        tour = input("Url del popup con tour (Inserte N si no hay tour): \n")
        if tour!="n" and tour!="N":
            lines.append("""<div class="elementor-element elementor-element-b909e2d elementor-widget elementor-widget-button" data-id="b909e2d" data-element_type="widget" data-widget_type="button.default">
                        <div class="elementor-widget-container">
                        <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" style="text-align: left;" role="button" """ + tour + """>
                        <span class="elementor-button-content-wrapper">
                        <span class="elementor-button-icon elementor-align-icon-left">
                        <i class="far fa-play-circle" aria-hidden="true"></i> </span>
                        <span class="elementor-button-text">Ver tour virtual 360º</span>
                        </span>
                        </a></div>
                        </div>
                        </div>""")


        gallery = input("Url del popup con la galería (Inserte N si no hay galería): \n")
        if gallery!="n" and gallery!="N":
            lines.append("""<div id="div-carousel" class="elementor-element elementor-element-94af6b5 elementor-widget elementor-widget-button" data-id="94af6b5" data-element_type="widget" data-widget_type="button.default">
                        <div class="elementor-widget-container">
                        <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" style="text-align: left;" role="button" """ + gallery + """>
                        <span class="elementor-button-content-wrapper">
                        <span class="elementor-button-icon elementor-align-icon-left">
                        <i class="far fa-eye" aria-hidden="true"></i> </span>
                        <span class="elementor-button-text">Ver más fotos de """ + name_subsection + """</span>
                        </span>
                        </a></div>
                        </div>
                        </div>""")       

        no_of_lines = int(input("\nNúmero de párrafos de la subsección: "))
        for j in range(no_of_lines):
            line = input()
            if gallery == "N" and tour!="N" and j == 0:
                lines.append("<p style=\"padding-top: 7%;\">" + line + "</p>") 
            elif tour == "N" and gallery!="N" and j == 0:
                lines.append("<p style=\"padding-top: 7%;\">" + line + "</p>") 
            else:
                lines.append("<p>" + line + "</p>")

        no_of_toggle_lines = int(input("\nNúmero de párrafos del toggle (Inserte 0 si no hay toggle): "))
        if no_of_toggle_lines != 0:
            toggle_lines = []
            for k in range(no_of_toggle_lines):
                line = input()
                toggle_lines.append(line + "<br>")
            toggle_content = """<button class="collapsible" type="button">Horarios y Servicios</button>
                    <div class="content">
                    """ + '\n'.join(toggle_lines)+ """
                    </div>"""
            lines.append(toggle_content)

    text = '\n'.join(lines)

    section_code = """<div class="tab-content">
    
    <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; margin-bottom: 10px;">""" + section_name + """ (360°)</h3>
    
    <div class="tab-img">

    """ + image_structure + """

    <div class="elementor-element elementor-element-715fc03 elementor-widget elementor-widget-button" data-id="715fc03" data-element_type="widget" data-widget_type="button.default">
    <div class="elementor-widget-container">
    <div class="elementor-button-wrapper"><a id="button-tour" class="elementor-button-link elementor-button elementor-size-sm" role="button" href="#""" + section_name + """-1">
    <span class="elementor-button-content-wrapper">
    <i class="far fa-play-circle" style="display: inline; font-size: 13px; margin-right: 5px;" aria-hidden="true"></i>
    <span class="elementor-button-text">Ver tour virtual en 360º
    <i class="fas fa-arrow-down" style="display: inline; font-size: 13px;"></i></span>
    </span></a></div>
    </div>
    </div>

    <div id="div-carousel" class="elementor-element elementor-element-ffa0974 elementor-widget elementor-widget-button" data-id="ffa0974" data-element_type="widget" data-widget_type="button.default">
    <div class="elementor-widget-container">
    <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" role="button" href="#""" + section_name + """-1">
    <span class="elementor-button-content-wrapper">
    <i class="far fa-eye" style="display: block-inline; font-size: 13px; margin-right: 5px;" aria-hidden="true"></i>
    <span class="elementor-button-text">Ver más fotos de """ + section_name + """
    <i class="fas fa-arrow-down" style="display: block-inline; font-size: 13px;"></i>
    </span>
    </span></a></div>
    </div>
    </div>

    """ + content + text + """

    </div>
    </div>
    """
    hs = open(section_name + " - " + hotel_name + ".html", 'w')
    hs.write(section_code)

    print(section_code)       

def food(
    section_name,
    hotel_name,
    image_structure,
    content,
    no_subsections
):
    lines = []
    for i in range(no_subsections):

        name_subsection = input("\nNombre del local: ")
        service = input("Tipo de local: ")

        if i == 0:
            lines.append(""" <h4 id="comida-1" style="display: block; font: 17px/29px Arial, serif; color: #292d34; font-weight: bold;">""" + name_subsection + """</h4>
                        <div class="etiqueta"><i class="fas fa-glass-cheers" style="margin-right: 5px;" aria-hidden="true"></i>""" + service + """</div>""")
        else:
            lines.append(""" <h4 style="display: block; font: 17px/29px Arial, serif; color: #292d34; font-weight: bold;">""" + name_subsection + """</h4>
                        <div class="etiqueta"><i class="fas fa-glass-cheers" style="margin-right: 5px;" aria-hidden="true"></i>""" + service + """</div>""")

        image_parts = []
        print("Código de imagen: ")
        for k in range(5):
            image_parts.append(input())
        image = '\n'.join(image_parts)
        lines.append(image)

        tour = input("Url del popup con tour (Inserte N si no hay tour): \n")
        if tour!="n" and tour!="N":
            lines.append("""<div class="elementor-element elementor-element-b909e2d elementor-widget elementor-widget-button" data-id="b909e2d" data-element_type="widget" data-widget_type="button.default">
                        <div class="elementor-widget-container">
                        <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" style="text-align: left;" role="button" """ + tour + """>
                        <span class="elementor-button-content-wrapper">
                        <span class="elementor-button-icon elementor-align-icon-left">
                        <i class="far fa-play-circle" aria-hidden="true"></i> </span>
                        <span class="elementor-button-text">Ver tour virtual 360º</span>
                        </span>
                        </a></div>
                        </div>
                        </div>""")


        gallery = input("Url del popup con la galería (Inserte N si no hay galería): \n")
        if gallery!="n" and gallery!="N":
            lines.append("""<div id="div-carousel" class="elementor-element elementor-element-94af6b5 elementor-widget elementor-widget-button" data-id="94af6b5" data-element_type="widget" data-widget_type="button.default">
                        <div class="elementor-widget-container">
                        <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" style="text-align: left;" role="button" """ + gallery + """>
                        <span class="elementor-button-content-wrapper">
                        <span class="elementor-button-icon elementor-align-icon-left">
                        <i class="far fa-eye" aria-hidden="true"></i> </span>
                        <span class="elementor-button-text">Ver más fotos de """ + name_subsection + """</span>
                        </span>
                        </a></div>
                        </div>
                        </div>""")       

        no_of_lines = int(input("\nNúmero de párrafos de la subsección: "))
        for j in range(no_of_lines):
            line = input()
            if gallery == "N" and tour!="N" and j == 0:
                lines.append("<p style=\"padding-top: 7%;\">" + line + "</p>") 
            elif tour == "N" and gallery!="N" and j == 0:
                lines.append("<p style=\"padding-top: 7%;\">" + line + "</p>") 
            else:
                lines.append("<p>" + line + "</p>")

        no_of_toggle_lines = int(input("\nNúmero de párrafos del toggle: "))
        toggle_lines = []
        for k in range(no_of_toggle_lines):
            line = input()
            toggle_lines.append(line + "<br>")
        toggle_content = """<button class="collapsible" type="button">Horarios y Servicios</button>
                <div class="content">
                """ + '\n'.join(toggle_lines)+ """
                </div>"""
        lines.append(toggle_content)

    text = '\n'.join(lines)
    if image_structure != "N":
        section_code = """<div class="tab-content">
        
        <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; margin-bottom: 10px;">""" + section_name + """ (360°)</h3>
        
        <div class="tab-img">

        """ + image_structure + """

        <div class="elementor-element elementor-element-715fc03 elementor-widget elementor-widget-button" data-id="715fc03" data-element_type="widget" data-widget_type="button.default">
        <div class="elementor-widget-container">
        <div class="elementor-button-wrapper"><a id="button-tour" class="elementor-button-link elementor-button elementor-size-sm" role="button" href="#comida-1">
        <span class="elementor-button-content-wrapper">
        <i class="far fa-play-circle" style="display: inline; font-size: 13px; margin-right: 5px;" aria-hidden="true"></i>
        <span class="elementor-button-text">Ver tour virtual en 360º
        <i class="fas fa-arrow-down" style="display: inline; font-size: 13px;"></i></span>
        </span></a></div>
        </div>
        </div>

        <div id="div-carousel" class="elementor-element elementor-element-ffa0974 elementor-widget elementor-widget-button" data-id="ffa0974" data-element_type="widget" data-widget_type="button.default">
        <div class="elementor-widget-container">
        <div class="elementor-button-wrapper"><a id="button-carousel" class="elementor-button-link elementor-button elementor-size-sm" role="button" href="#comida-1">
        <span class="elementor-button-content-wrapper">
        <i class="far fa-eye" style="display: block-inline; font-size: 13px; margin-right: 5px;" aria-hidden="true"></i>
        <span class="elementor-button-text">Ver más fotos de Restaurantes
        <i class="fas fa-arrow-down" style="display: block-inline; font-size: 13px;"></i>
        </span>
        </span></a></div>
        </div>
        </div>

        """ + content + text + """

        </div>
        </div>
        """
    else:
        section_code = """<div class="tab-content">
    
        <h3 style="text-align: center; background: white; border-radius: 0px 0px 30px 30px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); font: 17px Arial; font-weight: 800; padding-bottom: 5px; margin-bottom: 10px;">""" + section_name + """ (360°)</h3>
        
        <div class="tab-img">

        """ + content + text + """

        </div>
        </div>
        """
    hs = open(section_name + " - " + hotel_name + ".html", 'w')
    hs.write(section_code)

    print(section_code)  


menu = """ MENÚ: Tipos de secciones
1. Imagen, tour y galería.
2. Imagen y tour.
3. Imagen y galería.
4. Imagen
5. Solo el texto
6. Es una habitación
7. Es la sección de restaurantes
8. Sección con subsecciones (Por ejemplo: piscinas, bares...)
9. Sección de otros sitios para comer """
print(menu)

number = int(input("\nTipo de sección: "))

if number == 1:
    name = input("Nombre del hotel: ")
    section = input("Nombre de la sección: ")

    image_parts = []
    print("Código de imagen: ")
    for k in range(5):
        image_parts.append(input())
    image = '\n'.join(image_parts)

    tour = input("Url del popup con tour: \n")
    gallery = input("Url del popup con la galería: \n")
    t_gallery = input("Ver más fotos de")

    no_of_lines = int(input("Número de párrafos de contenido: "))
    lines = []
    for i in range(no_of_lines):
        line = input()
        if line != "empezar lista":
            lines.append("<p>" + line + "</p>")
        else:
            list_items = ["<ul>"]
            item = item = input()
            while item != "terminar lista":
                list_items.append("<li>" + item + "</li>")
                item = input()
            list_items.append("</ul>")
            list_text = '\n'.join(list_items)
            lines.append(list_text)


    text = '\n'.join(lines)

    toggle = input("¿Tiene toggle (Y/N)? ")
    if toggle == "y" or toggle == "Y":
        has = True
    else:
        has = False 

    image_tour_gallery(
        section,
        name,
        image,
        tour,
        gallery,
        t_gallery,
        text,
        has
    )
elif number == 2:
    name = input("Nombre del hotel: ")
    section = input("Nombre de la sección: ")

    image_parts = []
    print("Código de imagen: ")
    for k in range(5):
        image_parts.append(input())
    image = '\n'.join(image_parts)

    tour = input("Url del popup con tour: \n")

    no_of_lines = int(input("Número de párrafos de contenido: "))
    lines = []
    for i in range(no_of_lines):
        line = input()
        if line != "empezar lista":
            if i != 0:
                lines.append("<p>" + line + "</p>")
            else:
                lines.append("<p style=\"padding-top: 7%;\">" + line + "</p>")
        else:
            list_items = ["<ul>"]
            item = item = input()
            while item != "terminar lista":
                list_items.append("<li>" + item + "</li>")
                item = input()
            list_items.append("</ul>")
            list_text = '\n'.join(list_items)
            lines.append(list_text)
    text = '\n'.join(lines)

    toggle = input("¿Tiene toggle (Y/N)? ")
    if toggle == "y" or toggle == "Y":
        has = True
    else:
        has = False 

    image_tour(
        section,
        name,
        image,
        tour,
        text,
        has
    )
elif number == 3:
    name = input("Nombre del hotel: ")
    section = input("Nombre de la sección: ")

    image_parts = []
    print("Código de imagen: ")
    for k in range(5):
        image_parts.append(input())
    image = '\n'.join(image_parts)

    gallery = input("Url del popup con la galería: \n")
    t_gallery = input("Ver más fotos de")

    no_of_lines = int(input("Número de párrafos de contenido: "))
    lines = []
    for i in range(no_of_lines):
        line = input()
        if line != "empezar lista":
            if i != 0:
                lines.append("<p>" + line + "</p>")
            else:
                lines.append("<p style=\"padding-top: 7%;\">" + line + "</p>")
        else:
            list_items = ["<ul>"]
            item = item = input()
            while item != "terminar lista":
                list_items.append("<li>" + item + "</li>")
                item = input()
            list_items.append("</ul>")
            list_text = '\n'.join(list_items)
            lines.append(list_text)
    text = '\n'.join(lines)

    toggle = input("¿Tiene toggle (Y/N)? ")
    if toggle == "y" or toggle == "Y":
        has = True
    else:
        has = False 


    image_gallery(
        section,
        name,
        image,
        gallery,
        t_gallery,
        text,
        has
    )    
elif number == 4:
    name = input("Nombre del hotel: ")
    section = input("Nombre de la sección: ")
    
    image_parts = []
    print("Código de imagen: ")
    for k in range(5):
        image_parts.append(input())
    image = '\n'.join(image_parts)

    no_of_lines = int(input("Número de párrafos de contenido: "))
    lines = []
    for i in range(no_of_lines):
        line = input()
        if line != "empezar lista":
            lines.append("<p>" + line + "</p>")
        else:
            list_items = ["<ul>"]
            item = item = input()
            while item != "terminar lista":
                list_items.append("<li>" + item + "</li>")
                item = input()
            list_items.append("</ul>")
            list_text = '\n'.join(list_items)
            lines.append(list_text)
    text = '\n'.join(lines)

    toggle = input("¿Tiene toggle (Y/N)? ")
    if toggle == "y" or toggle == "Y":
        has = True
    else:
        has = False 

    image(
        section,
        name,
        image,
        text,
        has
    )  
elif number == 5:
    name = input("Nombre del hotel: ")
    section = input("Nombre de la sección: ")

    no_of_lines = int(input("Número de párrafos de contenido: "))
    lines = []
    for i in range(no_of_lines):
        line = input()
        if line != "empezar lista":
            lines.append("<p>" + line + "</p>")
        else:
            list_items = ["<ul>"]
            item = item = input()
            while item != "terminar lista":
                list_items.append("<li>" + item + "</li>")
                item = input()
            list_items.append("</ul>")
            list_text = '\n'.join(list_items)
            lines.append(list_text)
    text = '\n'.join(lines)

    toggle = input("¿Tiene toggle (Y/N)? ")
    if toggle == "y" or toggle == "Y":
        has = True
    else:
        has = False    

    only_content(
        section,
        name,
        text,
        has
    )  
elif number == 6:
    name = input("Nombre del hotel: ")
    section = input("Nombre de la sección: ")
    
    image_parts = []
    print("Código de imagen: ")
    for k in range(5):
        image_parts.append(input())
    image = '\n'.join(image_parts)

    tour = input("Url del popup con tour: \n")
    gallery = input("Url del popup con la galería: \n")
    subsections = int(input("¿Cuántas subsecciones tiene?: "))

    bedroom(
        section,
        name,
        image,
        tour,
        gallery,
        subsections
    )  
elif number == 7:
    name = input("Nombre del hotel: ")
    section = input("Nombre de la sección: ")
    
    image_parts = []
    print("Código de imagen: ")
    for k in range(5):
        image_parts.append(input())
    image = '\n'.join(image_parts)

    no_of_lines = int(input("Número de párrafos de introducción: "))
    lines = []
    for i in range(no_of_lines):
        line = input()
        lines.append("<p>" + line + "</p>")
    text = '\n'.join(lines)

    no_of_restaurants = int(input("Número de restaurantes: "))

    restaurants(
        section,
        name,
        image,
        text,
        no_of_restaurants
    ) 
elif number == 8:
    name = input("Nombre del hotel: ")
    section = input("Nombre de la sección: ")
    
    image_parts = []
    print("Código de imagen: ")
    for k in range(5):
        image_parts.append(input())
    image = '\n'.join(image_parts)

    no_of_lines = int(input("Número de párrafos de introducción: "))
    lines = []
    for i in range(no_of_lines):
        line = input()
        lines.append("<p>" + line + "</p>")
    text = '\n'.join(lines)

    no_of_subsections = int(input("Número de subsecciones: "))

    with_subsections(
        section,
        name,
        image,
        text,
        no_of_subsections
    )     
elif number == 9:
    name = input("Nombre del hotel: ")
    section = input("Nombre de la sección: ")
    
    image_parts = []
    print("Código de imagen (Inserte N si no hay imagen introductoria): \n")
    for k in range(5):
        image_parts.append(input())
    image = '\n'.join(image_parts)

    no_of_lines = int(input("Número de párrafos de introducción: "))
    lines = []
    for i in range(no_of_lines):
        line = input()
        if i == 0 and image == "N":
            lines.append("<p style=\"margin-bottom: -7%;\">" + line + "</p>")
        else:
            lines.append("<p>" + line + "</p>")
    text = '\n'.join(lines)

    no = int(input("Número de locales: "))

    food(
        section,
        name,
        image,
        text,
        no
    ) 
else:
    print("Insertó un valor que no corresponde a ninguno de los tipos")