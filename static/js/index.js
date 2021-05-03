// Tags a serem manusedas

var checkbox = document.getElementById('id_eh_palestrante');
var form = document.getElementsByClassName('sign-up-form')[0];
var paragraphs = form.getElementsByTagName('p');
let site = document.getElementById('id_site');
let minicurriculo = document.getElementById('id_minicurriculo');
let rede_social = document.getElementById('id_rede_social');

// Setando tags para um valor inicial

paragraphs[4].getElementsByTagName('label')[0].innerText = "Sou palestrante";
site.setAttribute('required', '');
minicurriculo.setAttribute('required', '');
rede_social.setAttribute('required', '');

// Verificar se o usuario eh um palestrante

checkbox.addEventListener('click', (e) => {
    if (e.target.checked) {
        paragraphs[5].style.display = 'block';
        paragraphs[6].style.display = 'block';
        paragraphs[7].style.display = 'block';
        site.setAttribute('required', '');
        minicurriculo.setAttribute('required', '');
        rede_social.setAttribute('required', '');
    } else {
        paragraphs[5].style.display = 'none';
        paragraphs[6].style.display = 'none';
        paragraphs[7].style.display = 'none';
        site.value = "";
        minicurriculo.value = "";
        rede_social.value = "";
        site.removeAttribute('required');
        minicurriculo.removeAttribute('required');
        rede_social.removeAttribute('required');
    }
});

function pegarPKEvento() {
    const urlParams = new URLSearchParams(location.search);
    const PKEvento = urlParams.get('evento');
    return PKEvento;
}