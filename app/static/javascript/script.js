const profileImg = document.getElementById('profile-img');
const profileMenu = document.getElementById('profile-menu');

profileImg.addEventListener('click', () => {
    if (profileMenu.style.display === 'block') {
        profileMenu.style.display = 'none';
    } else {
        profileMenu.style.display = 'block';
    }
});
