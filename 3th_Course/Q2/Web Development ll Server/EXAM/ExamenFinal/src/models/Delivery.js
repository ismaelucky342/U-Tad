/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      Examen Final - PW2S                               ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                                        ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        05/06/2026  -  17:30:13           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    05/06/2026  -  18:40:00           ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                                    */
/*      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             */
/*                                                                                                    */
/*      Github:                                           https://github.com/ismaelucky342            */
/*                                                                                                    */
/*====================================================================================================*/

// src/models/Delivery.js
const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');
const User = require('./User');

const Delivery = sequelize.define('Delivery', {
  // --- CAMPOS DEL DOMINIO ---
  id_paquete: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  shipment_name: {
    type: DataTypes.STRING(200),
    allowNull: false,
    references: { model: User , key: 'id' },
  },
  delivery_name: {
    type: DataTypes.STRING(200),
    allowNull: false,
    references: { model: User , key: 'id' },
  },
  DeliveryDate: {
    type: DataTypes.DATE,
    allowNull: false,
  },
}, {
  tableName: 'weather_data',
  timestamps: true,
});

// Relación: Un usuario puede tener muchos registros
User.hasMany(Delivery, { foreignKey: 'userId', as: 'Delivery' });
Delivery.belongsTo(User, { foreignKey: 'userId', as: 'uploader' });

module.exports = Delivery;
