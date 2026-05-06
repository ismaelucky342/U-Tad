const mongoose = require('mongoose');

const orderSchema = new mongoose.Schema(
  {
    orderNumber: {
      type: String,
      unique: true,
      required: true
    },
    paymentMethod: {
      type: String,
      required: [true, 'El método de pago es requerido'],
      enum: ['Credit Card', 'Debit Card', 'Cash', 'PayPal', 'Transfer'],
      default: 'Cash'
    },
    deliveryAddress: {
      type: String,
      required: false,
      minlength: [5, 'La dirección debe tener al menos 5 caracteres']
    },
    products: [
      {
        productId: {
          type: mongoose.Schema.Types.ObjectId,
          ref: 'Product',
          required: true
        },
        quantity: {
          type: Number,
          required: true,
          min: [1, 'La cantidad debe ser al menos 1']
        },
        price: {
          type: Number,
          required: true
        }
      }
    ],
    totalPrice: {
      type: Number,
      required: true,
      default: 0
    },
    status: {
      type: String,
      enum: ['Pending', 'Confirmed', 'Preparing', 'Ready', 'Delivered', 'Cancelled'],
      default: 'Pending'
    },
    customer: {
      name: String,
      phone: String,
      email: String
    }
  },
  { timestamps: true }
);

// Generar número de orden único antes de guardar
orderSchema.pre('save', async function (next) {
  if (!this.isNew) return next();
  
  try {
    const count = await this.constructor.countDocuments({});
    this.orderNumber = `ORD-${Date.now()}-${count + 1}`;
    next();
  } catch (error) {
    next(error);
  }
});

module.exports = mongoose.model('Order', orderSchema);
