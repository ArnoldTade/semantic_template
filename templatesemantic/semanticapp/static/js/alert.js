function confirmDeletion(event) {
    event.preventDefault();
    const url = event.currentTarget.getAttribute('href');

    Swal.fire({
        title: 'Delete this Employee?',
        text: "You won't be able to revert this!",
        showCancelButton: true,
        confirmButtonColor: '#943634',
        cancelButtonColor: '#877f79',
        confirmButtonText: 'Yes, delete it!',
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = url;
        }
    });
    return false;
}
