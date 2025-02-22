// Add delete confirmation dialog
document.querySelectorAll('.delete-link').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const pk = link.getAttribute('data-pk');
      if (confirm('Are you sure you want to delete this request?')) {
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = `/admin/customer_service/servicerequest/${pk}/delete/`;
        form.innerHTML += '<input type="hidden" name="csrfmiddlewaretoken" value="{{ csrf_token }}">';
        form.submit();
      }
    });
  });