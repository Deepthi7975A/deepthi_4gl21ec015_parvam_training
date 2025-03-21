function validateForm(event){
    event.preventDefault();

    const formFields = document.querySelectorAll("#registration_form .form-control, #registration_form .form-check-input");
    let isValied = true;

    function createErrorMessage(parentDiv, message){
        const errorMessage = document.createElement('div');
        errorMessage.classList.add('text-danger');
        errorMessage.innerText = message;
        parentDiv.appendChild(errorMessage);

        setTimeout(() => {
            errorMessage.remove();   
        }, 10000);
    }

    formFields.forEach(field => {
        let parentDiv = field.closest('.mb-3');
        const label = parentDiv.querySelector('label');

        const existingError = parentDiv.querySelector('.text-danger');
        if(existingError){
            existingError.remove();
        }

        if(field.id === 'phone_number'){
            const phonePattern = /^[6-9]\d{9}$/;
            if(field.value && !phonePattern.test(field.value.trim())){
                isValied = false;
                createErrorMessage(parentDiv, 'Phone number should contain only 10 digits and It should start with(6,7,8 or 9).');
            }
        }

        if(field.id === 'Email-ID'){
            const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}$/;
            if(field.value && !emailPattern.test(field.value.trim())){
                isValied = false;
                createErrorMessage(parentDiv, 'Please enter a valid email address.');
            }
        }

        if(field.id === 'aadhar_number'){
            const aadharPattern = /^\d{12}$/;
            if(field.value && !aadharPattern.test(field.value.trim())){
                isValied = false;
                createErrorMessage(parentDiv, 'Aadhar number should contain exactly 12 digits.');
            }
        }
        if(field.id === 'Pincode'){
            const pincodePattern = /^\d{6}$/;
            if(field.value && !pincodePattern.test(field.value.trim())){
                isValied = false;
                createErrorMessage(parentDiv, 'pin code should contain exactly 6 digits.');
            }
        }

        if(label && label.textContent.toLowerCase().includes('name')){
            const namePattern = /^[a-zA-Z\s.]+$/;
            if(field.value && !namePattern.test(field.value.trim())){
                isValied = false;
                createErrorMessage(parentDiv,`${label.textContent} can only contain alphabets, spaces & full-stop(period symbol).`);
            }
        }
    
        if(label && label.textContent.toLowerCase().includes('board')){
            const namePattern = /^[a-zA-Z\s.]+$/;
            if(field.value && !namePattern.test(field.value.trim())){
                isValied = false;
                createErrorMessage(parentDiv,`${label.textContent} can only contain alphabets, spaces & full-stop(period symbol).`);
            }
        }

        if(field.type === 'radio' || field.type === 'checkbox'){
            const radioChecked = document.querySelector(`input[name="${field.name}"]:checked`);
            if(!radioChecked){
                isValied = false;
                createErrorMessage(parentDiv, `${label.textContent} is required.`);
                console.log("Checked this block");
            }
        }else if(!field.value.trim()){
          isValied = false;
          createErrorMessage(parentDiv, `${label.textContent} is required.`);
        }
    });

    if(isValied){
        alert("Form summitted successfully!");
        document.getElementById("registration_form").submit();
        return true;
    }else{
        return false;
    }
}
    
