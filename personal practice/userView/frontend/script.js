

$(document).ready(() => {
    $('input[name="op"]').change(() => {
        $('#alluser, #newuser,#perticularuser,#updateuser,#deleteuser').hide()
        const choice = $('input[name="op"]:checked').val()
        $(`#${choice}`).removeClass('d-none')
        $(`#${choice}`).show()
    })
})


$('#datafetch').click(async () => {
    const response = await fetch('http://127.0.0.1:8000/api/v1/users', {
        method: 'GET',
        headers: {
            "Content-Type": "application/json"
        }
    })
    console.log(response)
    const data = await response.json()
    document.getElementById('databox').innerHTML=""
    data.forEach(user => {
        document.getElementById('databox').innerHTML += `id:${user.id} UserName:${user.username} Email:${user.email} <br>`
    });
})


$('#dataupload').click(async () => {
    const response = await fetch('http://127.0.0.1:8000/api/v1/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: document.getElementById('username').value,
            email: document.getElementById('email').value,
            password: document.getElementById('password').value
        })
    })

    if (!response.ok)
        return

    alert("user Created Successfully")
})


$('#dataperticular').click(async () => {
    const response = await fetch(`http://127.0.0.1:8000/api/v1/users/${document.getElementById('userid').value}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    const data = await response.json()
    console.log(data)
    document.getElementById('perticularbox').innerHTML = `id:${data.id} UserName:${data.username} Email:${data.email} <br>`
})


$('#dataupdate').click(async () => {
    console.log('imhereeeeeee')
    const response = await fetch(`http://127.0.0.1:8000/api/v1/users/${document.getElementById('updateid').value}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: document.getElementById('updateusername').value,
            email: document.getElementById('updateemail').value,
        })
    })

    console.log('IM HERE')
    if (response.ok)
        alert("update Successfully")

    alert(response.status)
    return
})


$('#delete').click(async () => {
    const response = await fetch(`http://127.0.0.1:8000/api/v1/users/${document.getElementById('deleteid').value}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })

    if (response.ok) {
        alert("deleted Successfully")
        return
    }
    alert(response.statusText+" User Not exists")

    console.log(response.statusText)
})