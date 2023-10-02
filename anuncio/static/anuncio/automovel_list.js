addEventListener('DOMContentLoaded',()=>{
    const tune=document.getElementById('tune')
    const barra_lateral=document.getElementById('barra_lateral')
    const barra_lista=document.getElementById('barra_lista')
    const barra_pesquisa=document.getElementById('barra_pesquisa')
    const p_itens=[...document.getElementsByClassName('p_itens')]
    const submit_tipo_automovel=[...document.getElementsByClassName('div_tipo_automovel')]

    document.getElementById('form_id').reset()

    submit_tipo_automovel.map((tipo_automovel)=>{
        tipo_automovel.addEventListener('click',()=>{
            tipo_automovel.nextElementSibling.click()
        })
    })
    
    p_itens.map((itens)=>{
        itens.addEventListener('click',()=>{
            itens.nextElementSibling.click()
        })
    })


    tune.addEventListener('click',()=>{
        if((barra_lateral.style.display == 'none')){
            barra_lateral.style.display = 'block'
            /* barra_lista.style.display = 'contents' */
            barra_pesquisa.style.marginTop = '5px !important;'
            barra_lista.style.position = 'absolute'
            barra_lista.style.paddingTop = '15px'
            barra_lista.style.top = '0px !important;'
            barra_lista.style.left = '393px'
            barra_lista.style.marginTop = '20px'
        }else if((barra_lateral.style.display !== 'none')){
            barra_lateral.style.display = 'none'
            barra_lista.style.display = 'block !important;'
            barra_pesquisa.style.marginTop = '80px !important;'
            barra_lista.style.position = 'absolute'
            barra_lista.style.paddingTop = '0px'
            barra_lista.style.top = '380px !important;'
            barra_lista.style.left = '0px'
            barra_lista.style.marginTop = '0px'
        }
    })
    
})