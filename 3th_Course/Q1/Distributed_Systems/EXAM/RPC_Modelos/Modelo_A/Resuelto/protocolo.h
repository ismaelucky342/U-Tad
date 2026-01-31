#ifndef PROTOCOLO_H
#define PROTOCOLO_H

enum personaMSGTypes {
    OP_SET_EDAD = 0,
    OP_GET_EDAD,
    OP_SET_NOMBRE,
    OP_GET_NOMBRE,
    OP_ACK,
    OP_ERROR
};

#endif
