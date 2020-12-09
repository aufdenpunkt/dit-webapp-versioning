(($) => {
  const CHECKBOX_SELECTOR = 'input[name$="in_stores"]';
  const SUBMIT_SELECTOR = 'input[type="submit"][name="_save"]';
  $(document).ready(() => {
    const $checkboxes = $(CHECKBOX_SELECTOR);
    const $submitButton = $(SUBMIT_SELECTOR);
    const handleCheckboxSelection = (event) => {
      event.preventDefault();
      $checkboxes.not(`[name=${event.target.name}]`).prop('checked', false);
      $submitButton.click();
    };
    $checkboxes.on('change', handleCheckboxSelection);
  });
})(django.jQuery);
