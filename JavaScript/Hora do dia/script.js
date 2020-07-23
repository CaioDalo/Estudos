function carregar() {
    var msg = window.document.getElementById('msg')
    var cmp = window.document.getElementById('cmp')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora > 0 && hora < 12) {
        cmp.innerHTML = 'Bom dia !'
        img.src = 'fotomanha.png'
        document.body.style.background = '#ccd6c3'
    } else if (hora <= 18) {
        cmp.innerHTML = 'Boa tarde !'
        img.src = 'fototarde.png'
        document.body.style.background = '#e39e6a'
    } else {
        cmp.innerHTML = 'Boa noite !'
        img.src = 'fotonoite.png'
        document.body.style.background = '#8c8883'
    }
}