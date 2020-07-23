function verificar(){
    var data = new Date()
    var atual = data.getFullYear()
    var ano = window.document.getElementById('txtano')
    var resultado = window.document.getElementById('res')
    if (ano.value.length == 0 || ano.value > atual) {
        window.alert('[ERRO] Verifique os dados e tente novamente')
    } else {
        var idade = atual - Number(ano.value)
        var fsex = document.getElementsByName('radsex')
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked) {
            if (idade <= 5) {
                var genero = 'menininho'
                img.setAttribute('src', 'menininho.png')
                // bebe  
            } else if (idade < 15) {
                var genero = 'menino'
                img.setAttribute('src', 'menino.png')
                // criança
            } else if (idade < 65) {
                var genero = 'homem'
                img.setAttribute('src', 'homem.png')
                //adulto
            } else {
                var genero = 'idoso'
                img.setAttribute('src', 'idoso.png')
                //idoso
            }
        } else {
            if (idade <= 5) {
                var genero = 'menininha'
                img.setAttribute('src', 'menininha.png')
                // bebe  
            } else if (idade < 15) {
                var genero = 'menina'
                img.setAttribute('src', 'menina.png')
                // criança
            } else if (idade < 65) {
                var genero = 'mulher'
                img.setAttribute('src', 'mulher.png')
                //adulto
            } else {
                var genero = idosa
                img.setAttribute('src', 'idosa.png')
                //idoso
            }
        }
        resultado.style.textAlign = 'center'
        resultado.innerHTML = `Detectamos ${genero} com idade de ${idade} anos`
        resultado.appendChild(img)
    }
   
}