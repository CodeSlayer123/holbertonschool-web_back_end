export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const outcome = mathFunction();
    queue.push(outcome);
  } catch (error) {
    queue.push(`${error.name}: ${error.message}`);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
