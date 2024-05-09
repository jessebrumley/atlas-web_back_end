export default function getListStudentIds(array) {
  if (Array.isArray(array)) {
    return array.map((res) => res.id);
  } else {
  return []
  }
}
