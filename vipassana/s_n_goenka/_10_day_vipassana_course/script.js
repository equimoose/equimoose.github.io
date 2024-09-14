
fetch(transcribed_discourse_url)
    .then(response => response.text())
    .then(data => {
        const transcription = [] // process_transcription(data)

        const content_el = document.getElementById("content")

        transcription.forEach(line => {
            content_el.innerText += (" " + line.text)
        })
    })
    .catch(error => console.error("Error fetching the file:", error))


// function process_transcription(data) {
//     let lines = data.split("\n")
//     lines = lines.slice(3) // Skip the first 3 header lines

//     const transcription = []

//     let current_line = get_new_line_object()

//     lines.forEach(line => {
//         line = line.trim()
//         if (line === "") return

//         if (line.match(/^\d+$/))
//         {
//             current_line.line_number = Number.parseInt(line, 10)
//             return
//         }

//         if (line.match(/^\d{2}:\d{2}:\d{2}/))
//         {
//             current_line.time = line
//             return
//         }

//         current_line.text = line
//         transcription.push(current_line)
//         current_line = get_new_line_object()
//     })

//     return transcription
// }


function get_new_line_object() {
    return {
        line_number: -1,
        time: "",
        text: ""
    }
}
