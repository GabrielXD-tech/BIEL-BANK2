const tabs = document.querySelectorAll('.tab');
const tabContents = document.querySelectorAll('.content');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const tabId = tab.dataset.tab;

    // Ativar a aba clicada
    tabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');

    // Mostrar o conteúdo correspondente e ocultar os outros
    tabContents.forEach(content => {
      if (content.id === tabId + '-content') {
        content.style.display = 'block';
      } else {
        content.style.display = 'none';
      }
    });
  });
});
