document.getElementById('lead-form').addEventListener('submit', async function(e) {
    e.preventDefault(); // Evita que la página parpadee o se recargue

    // Extraemos los datos del formulario
    const leadData = {
        nombre: document.getElementById('nombre').value,
        telefono: document.getElementById('telefono').value,
        correo: document.getElementById('correo').value,
        interes: document.getElementById('modelo-interes').value,
        fecha: new Date().toISOString(),
        origen: { fuente: 'prueba_local', campana: 'directo' }
    };

    // Cambiamos el texto del botón para dar retroalimentación
    const btnSubmit = document.querySelector('button[type="submit"]');
    btnSubmit.innerText = "Procesando...";

    try {
        // Apuntamos a tu servidor LOCAL en el puerto 8000
        const response = await fetch('http://127.0.0.1:8000/webhook/lead', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(leadData)
        });

        if (response.ok) {
            alert("¡Conexión exitosa! Revisa la terminal de Python.");
            btnSubmit.innerText = "Enviar y contactar por WhatsApp";
            // Opcional: limpiar el formulario
            document.getElementById('lead-form').reset();
        } else {
            alert("Error en la respuesta del servidor.");
            btnSubmit.innerText = "Enviar y contactar por WhatsApp";
        }
    } catch (error) {
        console.error("Error:", error);
        alert("Asegúrate de que el servidor FastAPI esté corriendo.");
        btnSubmit.innerText = "Enviar y contactar por WhatsApp";
    }
});