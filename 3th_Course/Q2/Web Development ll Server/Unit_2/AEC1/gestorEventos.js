/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC1 - PWIC                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                                        ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        17/03/2026  -  01:07:13           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    21/03/2026  -  12:49:00           ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                                    */
/*      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             */
/*                                                                                                    */
/*      Github:                                           https://github.com/ismaelucky342            */
/*                                                                                                    */
/*====================================================================================================*/

const EventEmitter = require("events");

class GestorEventos extends EventEmitter {
	/**
	 * Me gusta tener un wrapper claro :)
	 */
	registrar(evento, handler) {
		this.on(evento, handler);
	}

	/**
	 * Emito eventos desde un unico sitio para poder centralizar cambios
	 */
	emitir(evento, payload) {
		this.emit(evento, payload);
	}

	/**
	 * Version de una sola vez para eventos puntuales, la dejo lista por si la necesito.
	 */
	registrarUnaVez(evento, handler) {
		this.once(evento, handler);
	}
}

module.exports = GestorEventos;
