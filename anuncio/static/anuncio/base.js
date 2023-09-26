const nav=document.getElementById('nav_user')
/* user_links.style.display = 'flex' */
nav.addEventListener('mouseenter',()=>{
    const user_links=document.getElementById('user_links')
    user_links.style.display = 'flex'
    console.log(nav)
})
nav.addEventListener('mouseleave',()=>{
    const user_links=document.getElementById('user_links')
    user_links.style.display = 'none'
    console.log(nav)
})



