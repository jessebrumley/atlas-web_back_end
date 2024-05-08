import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const classrooms = [];

  classrooms.push(new ClassRoom(19));
  classrooms.push(new ClassRoom(20));
  classrooms.push(new ClassRoom(34));

  return classrooms;
}
