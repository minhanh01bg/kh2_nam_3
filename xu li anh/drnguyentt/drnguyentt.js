const ide = document.querySelector('#vplide');
const ideUploadForm = document.querySelector('#vplide form');

const resetFileName = () => {
  document.querySelector('#vplide form input').value = '';
};

const displayUploadForm = () => {
  ideUploadForm.style.display = 'block';
  const resetFileNameBtn = document.createElement('button');
  resetFileNameBtn.innerText = 'Reset file name';
  resetFileNameBtn.style.marginTop = '10px';
  resetFileNameBtn.style.backgroundColor = '#f00';
  resetFileNameBtn.style.color = '#fff';
  resetFileNameBtn.style.borderColor = '#fff';
  resetFileNameBtn.style.borderWidth = '1px';
  resetFileNameBtn.addEventListener('click', resetFileName);
  resetFileNameBtn.addEventListener('mouseover', () => {
    resetFileNameBtn.style.backgroundColor = '#c00';
  });
  resetFileNameBtn.addEventListener('mouseout', () => {
    resetFileNameBtn.style.backgroundColor = '#f00';
  });
  ide.appendChild(resetFileNameBtn);
};

if (ide) {
  displayUploadForm();
};