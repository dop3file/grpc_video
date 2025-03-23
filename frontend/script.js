const persons = document.getElementById('persons');
const eventSource = new EventSource('http://0.0.0.0:8000/fake_personal/stream');

eventSource.onopen = () => {
    console.log('EventSource connected');
}
function generate() {
    eventSource.onmessage = function(event) {
        person_card = document.createElement("div");
        person = JSON.parse(event.data)
        console.log(person)
        person_card.innerHTML = `Name - ${person["name"]}<br>Address - ${person["address"]}<br>City - ${person["city"]}<br><br>`
        person_card.id = "person_card"
        persons.appendChild(person_card);
    };
}

