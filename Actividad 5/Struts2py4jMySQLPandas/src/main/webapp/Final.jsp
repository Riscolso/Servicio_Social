<!DOCTYPE html>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="s" uri="/struts-tags" %>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Jython</title>
  </head>
  <body>
      <h2>Valores extraídos de python</h2>
          <h2>Usando MySQL y Pandas </h2>
      Grupo: <s:property value="modelo.grupo" /><br/>
      Promedio de grupo: <s:property value="modelo.promedio" /><br/>
  </body>
</html>