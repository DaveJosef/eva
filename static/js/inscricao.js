var cancel_btn = document.getElementById('cancelar-inscricao-btn');
var inscricao_btn = document.getElementById('inscricao-box-btn');
var event_actions = document.getElementById('event-actions');

if (cancel_btn) {
    console.log('Funcionando');
    event_actions.removeChild(inscricao_btn);
}