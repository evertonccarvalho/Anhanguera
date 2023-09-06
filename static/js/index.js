function formatInput(input) {
  // Remove qualquer caractere não numérico
  input.value = input.value.replace(/\D/g, "");

  // Adicione a vírgula após o primeiro dígito
  if (input.value.length === 3) {
    input.value = input.value.slice(0, 1) + "," + input.value.slice(1);
  }
}
