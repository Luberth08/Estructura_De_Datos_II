$(document).ready(function() {

    // VARIABLES --------------------------------------------------------------------------------------------------------------------------------
    let turno = parseInt(document.getElementById('turno_ini').dataset.value)
    let dados = JSON.parse(document.getElementById('dados_ini').dataset.value)
    let jugadores = JSON.parse(document.getElementById('jugadores_ini').dataset.value)
    let estrategia_tiro = [0, 0, 0, 0, 0]
    let jugada = 0
    let sw_final = false

    // CONSTANTES --------------------------------------------------------------------------------------------------------------------------------
    const btn_userlanzar = $("#user_lanzar")
    const ia_points = $("#ia_points")
    const user_points = $("#user_points")
    const ult_jugada = $("#ult_jugada")
    const tgl_selectdices = $(".select_dice")
    const tgl_jugada = $(".jugada")

    statemachine() 

    if (jugadores[turno]['nombre'] == 'IA'){
        setTimeout(function() {
            lanzar_dados()
        }, 2000)
    }

    // MANEJADORES --------------------------------------------------------------------------------------------------------------------------------
    btn_userlanzar.click(function() {
        lanzar_dados()
    })


    tgl_selectdices.click(function() {
        select_dices.call(this)
    })


    tgl_jugada.click(function() {
        select_jugada.call(this)
    })


    // MANEJO DE ESTADOS --------------------------------------------------------------------------------------------------------------------------
    function statemachine(){

        // Para los dados
        for (let i = 0; i < 5; i++) { 
            $(`#dice${i+1} .dado-imagen`).attr('src', RUTAS_DADOS[dados[i]-1]);
        }

        // Para los puntos de la IA
        ia_points.text(jugadores[1]['puntos'])

        // Para los puntos del Jugador
        user_points.text(jugadores[0]['puntos'])    

        // Para los seleccionadores de dados
        // Para la seleccion de la jugada 
        if(jugadores[turno]['tiros'] == 1){
            tgl_selectdices.prop('disabled', false)

            for(let i = 0; i < 5; i++) {
                estrategia_tiro[i] = +(tgl_selectdices.filter(`[data-dice="${i+1}"]`).hasClass('active'))
            }

            for(let i = 1; i <= 6; i++) {
                tgl_jugada.filter(`[data-value="${i}"]`).prop('disabled', jugadores[turno]['libreta'].includes(i)) 
            }
        }
        else{
            tgl_selectdices.prop('disabled', true)
            tgl_selectdices.toggleClass('active', false)

            tgl_jugada.prop('disabled', true)
            tgl_jugada.toggleClass('active', false)

            estrategia_tiro = [1, 1, 1, 1, 1]
        }

        // Para los botones de lanzar
        b = true
        for(let i = 1; i <= 6; i++) {
            if (tgl_jugada.filter(`[data-value="${i}"]`).prop('disabled') == false){
                b = false
            }
        }
        if(jugadores[turno]['nombre'] == 'Jugador'){  
            tgl_selectdices.prop('disabled', false)
            tgl_jugada.prop('disabled', false)     
            if (estrategia_tiro.some(val => val === 1) && (jugada!=0 || b)){
                btn_userlanzar.prop('disabled', false)
            }
            else{
                btn_userlanzar.prop('disabled', true)
            }
        }
        else{
            btn_userlanzar.prop('disabled', true)
            tgl_selectdices.prop('disabled', true)
            tgl_jugada.prop('disabled', true)
        }

        if(jugadores[0]['libreta'].length == 6 && jugadores[1]['libreta'].length == 6){
            console.log("El juego ha terminado. No hay más jugadas posibles.")
            sw_final = true
            return
        }
        /*
        console.log("gfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfgdfg")
        console.log("estrategia de tiro:")
        console.log(estrategia_tiro)
        console.log("apuesta:")
        console.log(jugada)
        console.log("Jugador:")
        console.log(jugadores[0]['libreta'])
        console.log("IA:")
        console.log(jugadores[1]['libreta'])
        */
        
    }

    
    // FUNCIONES --------------------------------------------------------------------------------------------------------------------------
    function lanzar_dados(){
        $.ajax({
            url: LANZAR_DADOS_URL,
            type: "POST",
            data: {
                'csrfmiddlewaretoken': CSRF_TOKEN,  
                'est_tiro': JSON.stringify(estrategia_tiro),
                'jugada': JSON.stringify(jugada),
            },
            success: function(response){
                if (!response.success) {
                    return
                }

                turno = response.turno
                dados = response.dados
                jugadores = response.jugadores   
                jugada = 0
                statemachine()     
                actualizar_ultjugada(response.ult_jugada)

                if(jugadores[turno]['nombre'] == 'IA' && sw_final == false){
                    setTimeout(function() {
                        lanzar_dados()
                    }, 2000)
                }
            },
            error: function(xhr, status, error) {
                console.error("Error al lanzar dados:", error)
                alert("Ocurrió un error. Recarga la página e intenta nuevamente.")
            }
        })
    }


    function select_dices(){
        if($(this).prop('disabled')){
            return
        }

        const i = $(this).data('dice')
        sw = tgl_selectdices.filter(`[data-dice="${i}"]`).hasClass('active')
        tgl_selectdices.filter(`[data-dice="${i}"]`).toggleClass('active', !sw)     

        statemachine()
    }


    function select_jugada(){
        if($(this).prop('disabled')){
            return
        }   

        const nueva_jugada = $(this).data('value')

        if(nueva_jugada == jugada){
            $(this).toggleClass('active', false)
            jugada = 0
        }
        else{
            tgl_jugada.toggleClass('active', false)
            $(this).toggleClass('active', true)
            jugada = nueva_jugada
        }

        statemachine()
    }


    function actualizar_ultjugada(info_jugada){
        text = ""
        switch (info_jugada) {
        case 6:
            text = "LA GRANDE"
            break;
        case 5:
            text = "POCKER"
            break;
        case 4:
            text = "LA FULL"
            break;
        case 3:
            text = "ESCALERA"
            break;
        case 2:
            text = "TRICA"
            break;
        case 1:
            text = "PAR"
            break;
        default:
            text = "Nada"
        }
        ult_jugada.text(text)
    }
});



