/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC3 - PW2S                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                                        ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        15/05/2026  -  01:07:13           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    23/05/2026  -  12:49:00           ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                                    */
/*      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             */
/*                                                                                                    */
/*      Github:                                           https://github.com/ismaelucky342            */
/*                                                                                                    */
/*====================================================================================================*/

const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const userSchema = new mongoose.Schema(
  {
    fullName: {
      type: String,
      required: [true, 'El nombre completo es requerido'],
      trim: true,
      minlength: [3, 'El nombre debe tener al menos 3 caracteres']
    },
    username: {
      type: String,
      required: [true, 'El username es requerido'],
      unique: true,
      trim: true,
      minlength: [3, 'El username debe tener al menos 3 caracteres'],
      match: [/^[a-zA-Z0-9_]+$/, 'El username solo puede contener letras, números y guiones bajos']
    },
    email: {
      type: String,
      required: [true, 'El correo es requerido'],
      unique: true,
      lowercase: true,
      match: [/^[^\s@]+@[^\s@]+\.[^\s@]+$/, 'Por favor ingrese un correo válido']
    },
    phone: {
      type: String,
      required: [true, 'El teléfono es requerido'],
      match: [/^[\d\s\-\+\(\)]+$/, 'El teléfono debe ser válido']
    },
    position: {
      type: String,
      required: [true, 'El cargo/puesto es requerido'],
      enum: ['Admin', 'Manager', 'Staff', 'Chef', 'Delivery'],
      default: 'Staff'
    },
    password: {
      type: String,
      required: [true, 'La contraseña es requerida'],
      select: false,
      minlength: [6, 'La contraseña debe tener al menos 6 caracteres']
    },
    isFirstUser: {
      type: Boolean,
      default: false
    }
  },
  { timestamps: true }
);

// Hash de contraseña antes de guardar
userSchema.pre('save', async function (next) {
  if (!this.isModified('password')) {
    return next();
  }

  try {
    const salt = await bcrypt.genSalt(10);
    this.password = await bcrypt.hash(this.password, salt);
    next();
  } catch (error) {
    next(error);
  }
});

// Método para comparar contraseñas
userSchema.methods.matchPassword = async function (enteredPassword) {
  return await bcrypt.compare(enteredPassword, this.password);
};

// Ocultar contraseña al convertir a JSON
userSchema.methods.toJSON = function () {
  const user = this.toObject();
  delete user.password;
  return user;
};

module.exports = mongoose.model('User', userSchema);
