### ✅ **1. Trigger para registrar empleados eliminados**

CREATE TRIGGER guardar_empleado_eliminado
BEFORE DELETE ON Empleados
FOR EACH ROW
BEGIN
    INSERT INTO EmpleadosEliminados (
        EmpleadoID,
        NombreEmpleado,
        DepartamentoID,
        FechaContratacion
    ) VALUES (
        OLD.EmpleadoID,
        OLD.NombreEmpleado,
        OLD.DepartamentoID,
        OLD.FechaContratacion
    );
END;


---

### ✅ **2. Trigger para asignar `CURDATE()` si no se especifica `FechaAsignacion`**


CREATE TRIGGER asignar_fecha_asignacion
BEFORE INSERT ON Asignaciones
FOR EACH ROW
BEGIN
    IF NEW.FechaAsignacion IS NULL THEN
        SET NEW.FechaAsignacion = CURDATE();
    END IF;
END;


---

### ✅ **3. Trigger para registrar cambios de departamento**

CREATE TRIGGER registrar_cambio_departamento
BEFORE UPDATE ON Empleados
FOR EACH ROW
BEGIN
    IF OLD.DepartamentoID != NEW.DepartamentoID THEN
        INSERT INTO Historial_Departamentos (
            EmpleadoID,
            DepartamentoAnterior,
            DepartamentoNuevo,
            FechaCambio
        ) VALUES (
            OLD.EmpleadoID,
            OLD.DepartamentoID,
            NEW.DepartamentoID,
            CURDATE()
        );
    END IF;
END;

### 4. Trigger para evitar sueldos negativos al insertar o actualizar empleados
CREATE TRIGGER evitar_sueldo_negativo
BEFORE INSERT ON Empleados
FOR EACH ROW
BEGIN
	IF NEW.Sueldo < 0 THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'El sueldo no puede ser negativo';
	END IF;
END;

CREATE TRIGGER evitar_sueldo_negativo_update
BEFORE UPDATE ON Empleados
FOR EACH ROW
BEGIN
	IF NEW.Sueldo < 0 THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'El sueldo no puede ser negativo';
	END IF;
END;

### 5. Trigger para registrar asignaciones eliminadas
CREATE TRIGGER guardar_asignacion_eliminada
BEFORE DELETE ON Asignaciones
FOR EACH ROW
BEGIN
	INSERT INTO AsignacionesEliminadas (
		AsignacionID,
		EmpleadoID,
		ProyectoID,
		FechaAsignacion
	) VALUES (
		OLD.AsignacionID,
		OLD.EmpleadoID,
		OLD.ProyectoID,
		OLD.FechaAsignacion
	);
END;

### 6. Trigger para actualizar la fecha de modificación de empleados
CREATE TRIGGER actualizar_fecha_modificacion
BEFORE UPDATE ON Empleados
FOR EACH ROW
BEGIN
	SET NEW.FechaModificacion = NOW();
END;
