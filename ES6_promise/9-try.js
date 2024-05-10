export default function guardrail(mathFunc) {
  const queue = [];

  try {
    queue.push(mathFunc());
  } catch (e) {
    queue.push(`Error: ${e.message}`);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
