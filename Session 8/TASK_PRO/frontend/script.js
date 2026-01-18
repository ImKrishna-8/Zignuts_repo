function checkAuth() {
    const token = localStorage.getItem('access');

    const loginBtn = document.getElementById('btn-login');
    const signupBtn = document.getElementById('btn-signup');
    const logoutBtn = document.getElementById('btn-logout');
    const sortdate = document.getElementById('sortdate');
    const searchtitle = document.getElementById('searchtitle');
    const filterpriority = document.getElementById('filterpriority');
    const alltask = document.getElementById('alltask');
    const createtask = document.getElementById('createtask');
    const pendingtask = document.getElementById('pendingtask');

    if (token) {
        if (logoutBtn) logoutBtn.style.display = 'block';
        if (loginBtn) loginBtn.style.display = 'none';
        if (signupBtn) signupBtn.style.display = 'none';

        if (alltask) alltask.style.display = 'block';
        if (createtask) createtask.style.display = 'block';
        if (pendingtask) pendingtask.style.display = 'block';
        if (sortdate) sortdate.style.display = 'block';
        if (searchtitle) searchtitle.style.display = 'block';
        if (filterpriority) filterpriority.style.display = 'block';

    } else {
        if (logoutBtn) logoutBtn.style.display = 'none';
        if (loginBtn) loginBtn.style.display = 'block';
        if (signupBtn) signupBtn.style.display = 'block';
        if (sortdate) sortdate.style.display = 'none';
        if (searchtitle) searchtitle.style.display = 'none';
        if (filterpriority) filterpriority.style.display = 'none';
        if (alltask) alltask.style.display = 'none';
        if (createtask) createtask.style.display = 'none';
        if (pendingtask) pendingtask.style.display = 'none';
    }
}
document.addEventListener('DOMContentLoaded', checkAuth);

// logout
document.getElementById('btn-logout').addEventListener('click', () => {
    localStorage.removeItem('access');
    alert("Logout successful")
    window.location.reload();

    checkAuth(); // Refresh UI
});

// Login
async function login_user() {

    const response = await fetch('http://127.0.0.1:8000/api/v1/token/', {
        method: 'POST',
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify({
            username: document.getElementById("username").value,
            password: document.getElementById("password").value
        })
    })

    const data = await response.json()
    if (response.ok) {
        localStorage.setItem('access', data.access)
        localStorage.setItem('refresh', data.refresh)
        alert("Login successful");
        window.location.reload();
    } else {
        alert("Invalid credentials");
    }
}


async function signup_user() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/v1/users/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: document.getElementById("signup_username").value,
                email: document.getElementById("signup_email").value,
                password: document.getElementById("signup_password").value
            })
        });

        const data = await response.json();

        if (response.ok) {
            alert("Signup successful");
            console.log(data); 
        } else {
 
            alert(JSON.stringify(data));
        }

    } catch (error) {
        console.error("Network error:", error);
        alert("Server not reachable");
    }
    window.location.reload();

}


async function load_data() {

    const token = localStorage.getItem('access')
    if (token) {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/v1/tasks/', {
                method: "GET",
                headers: {
                    "Authorization": "Bearer " + token,
                    "Content-Type": "application/json"
                },
            });
            const data = await response.json();
            const container = document.getElementById("task-container");
            const noTaskMsg = document.getElementById("no-task-msg");


            // Priority order mapping
            const priorityOrder = {
                high: 1,
                medium: 2,
                low: 3
            };

            // Sort tasks by priority
            data.sort((a, b) => {
                return priorityOrder[a.priority] - priorityOrder[b.priority];
            });

            container.innerHTML = "";

            if (!data || data.length === 0) {
                noTaskMsg.style.display = "block";
                container.style.display = "none";
                return;
            }

            noTaskMsg.style.display = "none";
            container.style.display = "flex";

            data.forEach(task => {
                container.innerHTML += createTaskCard(task);
            });


        } catch (error) {
            console.error("Network error:", error);
            alert("Server not reachable");
        }
        // window.location.reload();
    }
}

async function deleteTask(id) {
    if (!confirm("Delete this task?")) return;
    const token = localStorage.getItem('access')

    await fetch(`http://127.0.0.1:8000/api/v1/tasks/${id}/`, {
        method: "DELETE",
        headers: {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        },
    });

    load_data();
}
async function create_task() {
    const token = localStorage.getItem('access');

    if (!token) {
        alert("Please login first");
        return;
    }

    const title = document.getElementById('task_title').value;
    const description = document.getElementById('task_description').value;
    const due_date = document.getElementById('task_due_date').value;
    const priority = document.getElementById('task_priority').value;
    const status = document.getElementById('task_status').value;

    if (!title || !priority || !status) {
        alert("Title, Priority and Status are required");
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:8000/api/v1/tasks/', {
            method: "POST",
            headers: {
                "Authorization": "Bearer " + token,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                title: title,
                description: description,
                due_date: due_date || null,
                priority: priority,
                status: status
            })
        });

        const data = await response.json();

        if (response.ok) {
            alert("Task created successfully");

  
            const modal = bootstrap.Modal.getInstance(
                document.getElementById('createtaskmodal')
            );
            modal.hide();


            load_data();
        } else {
            console.error(data);
            alert("Error creating task");
        }

    } catch (error) {
        console.error("Error:", error);
    }
}

function createTaskCard(task) {

    let statusBadge = "secondary";
    if (task.status === "approved") statusBadge = "success";
    else if (task.status === "rejected") statusBadge = "danger";
    else if (task.status === "pending") statusBadge = "warning";

    let priorityBadge = "secondary";
    if (task.priority === "high") priorityBadge = "danger";
    else if (task.priority === "medium") priorityBadge = "warning";
    else if (task.priority === "low") priorityBadge = "success";

    return `
        <div class="col-md-4">
            <div class="card h-100 shadow-sm">
                <div class="card-body">
                    <h5 class="card-title">${task.title}</h5>

                    <p class="" style="color:white">
                        ${task.description}
                    </p>

                    <p class="mb-1" >
                        <strong>Due:</strong> ${task.due_date}
                    </p>

                    <span style="color:black" class="badge bg-${priorityBadge} me-2" >
                        Priority: ${task.priority}
                    </span>

                    <span  style="color:black" class="badge bg-${statusBadge}">
                        ${task.status}
                    </span>
                </div>

                <div class="card-footer bg-transparent border-top-0">
                    <button class="btn btn-sm btn-outline-primary"
                    data-bs-toggle="modal"
                data-bs-target="#editTaskModal"
                        onclick="editTask(${task.id})">
                        Edit
                    </button>

                    <button class="btn btn-sm btn-outline-danger"
                        onclick="deleteTask(${task.id})">
                        Delete
                    </button>
                </div>
            </div>
        </div>
    `;
}

function editTask(taskId) {
    
    const task = allTasks.find(t => t.id === taskId); 

    if (!task) return;

    // Set values in modal
    document.getElementById('edit_task_id').value = task.id;
    document.getElementById('edit_task_title').value = task.title;
    document.getElementById('edit_task_description').value = task.description;
    document.getElementById('edit_task_due_date').value = task.due_date;
    document.getElementById('edit_task_priority').value = task.priority.toLowerCase();
    document.getElementById('edit_task_status').value = task.status.toLowerCase();
}

async function updateTask() {
    const taskId = document.getElementById('edit_task_id').value;

    const updatedTask = {
        title: document.getElementById('edit_task_title').value,
        description: document.getElementById('edit_task_description').value,
        due_date: document.getElementById('edit_task_due_date').value,
        priority: document.getElementById('edit_task_priority').value,
        status: document.getElementById('edit_task_status').value
    };

    const token = localStorage.getItem('access'); // if using JWT

    try {
        const response = await fetch(`http://127.0.0.1:8000/api/v1/tasks/${taskId}/`, {
            method: "PUT",
            headers: {
                "Authorization": "Bearer " + token,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(updatedTask)
        });

        console.log("Hellooo");
        console.log(response.ok)
        if (response.ok) {
            const data = await response.json();
            alert("Task updated successfully!");
            // Close modal
            const editModal = bootstrap.Modal.getInstance(document.getElementById('editTaskModal'));
            editModal.hide();

            // Optionally refresh tasks
            load_data();
        } else {
            const errorData = await response.json();
            console.error(errorData);
            alert("Failed to update task");
        }
    } catch (error) {
        console.error(error);
        alert("An error occurred");
    }
}


// For extra purpose

let allTasks = [];

async function getting_task(status = '') {
    const token = localStorage.getItem('access');

    let url = 'http://127.0.0.1:8000/api/v1/tasks/';
    if (status) {
        url += `?status=${status}`;
    }

    const response = await fetch(url, {
        headers: {
            "Authorization": "Bearer " + token
        }
    });

    allTasks = await response.json(); 
}

getting_task()

function sortByDueDate() {
    const container = document.getElementById("task-container");
    const noTaskMsg = document.getElementById("no-task-msg");

    const data = [...allTasks].sort((a, b) => {
        if (!a.due_date) return 1;
        if (!b.due_date) return -1;
        return new Date(a.due_date) - new Date(b.due_date);
    });
    console.log(allTasks);
    console.log(data);
    container.innerHTML = "";

    if (data.length === 0) {
        noTaskMsg.style.display = "block";
        container.style.display = "none";
        return;
    }

   
    noTaskMsg.style.display = "none";
    container.style.display = "flex"; 

    data.forEach(task => {
        container.innerHTML += createTaskCard(task);
    });
}

function searchTasks() {
    const searchValue = document.getElementById('searchtitle').value.toLowerCase();

    const data = allTasks.filter(task =>
        task.title.toLowerCase().includes(searchValue)
    );

    const container = document.getElementById("task-container");
    const noTaskMsg = document.getElementById("no-task-msg");

    console.log(allTasks);
    console.log(data);
    container.innerHTML = "";

    if (data.length === 0) {
        noTaskMsg.style.display = "block";
        container.style.display = "none";
        return;
    }


    noTaskMsg.style.display = "none";
    container.style.display = "flex";

    data.forEach(task => {
        container.innerHTML += createTaskCard(task);
    });
}



function filterByPriority() {
    const priority = document.getElementById('filterpriority').value;

    if (priority === "") {
        load_data()
        return;
    }

    const data = allTasks.filter(task =>
        task.priority === priority
    );

    const container = document.getElementById("task-container");
    const noTaskMsg = document.getElementById("no-task-msg");

    console.log(allTasks);
    console.log(data);
    container.innerHTML = "";

    if (data.length === 0) {
        noTaskMsg.style.display = "block";
        container.style.display = "none";
        return;
    }


    noTaskMsg.style.display = "none";
    container.style.display = "flex"; // or "block"

    data.forEach(task => {
        container.innerHTML += createTaskCard(task);
    });
}

