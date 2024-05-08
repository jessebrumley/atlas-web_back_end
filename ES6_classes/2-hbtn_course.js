export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new Error('Name must be a string');
    } else {
      this._name = name;
    }

    if (typeof length !== 'number' || length <= 0) {
      throw new Error('Length must be a positive number');
    } else {
      this._length = length;
    }

    if (!Array.isArray(students)) {
      throw new Error('Students must be an array of names');
    } else {
      this._students = students;
    }
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName !== 'string') {
      throw new Error('Name must be a string');
    } else {
      this._name = newName;
    }
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength !== 'number' || newLength <= 0) {
      throw new Error('Length must be a positive number');
    } else {
      this._length = newLength;
    }
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (!Array.isArray(newStudents)) {
      throw new Error('Students must be an array of names');
    } else {
      this._students = newStudents;
    }
  }
}
