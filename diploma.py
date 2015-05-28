# -*- coding: utf-8 -*-

from lxml import etree
import csv

target_namespace = 'http://sample.ru/login'
definitions_name = 'LoginInterface'
attributeFormDefault = 'unqualified'
elementFormDefault = 'unqualified'
element_name = 'login'
sub_element_name = 'login'
sub_element_type = 'xs:string'
message_name = 'login'
part_element = 'tns:login'
part_name = 'parameters'
port_type_name = 'LoginInterface'
operation_name = 'login'
operation_input_name = 'login'
operation_input_message = 'tns:login'
operation_output_name = 'loginResponse'
operation_output_message = 'loginResponse'
binding_name = 'ServiceLoginSoapBinding'
binding_type = 'tns:LoginInterface'
soap_binding_style = 'document'

wsdl_operation_name = 'login'
soap_operation_style = 'document'
wsdl_input_name = 'login'
soap_body_use = 'literal'
wsdl_output_name = 'loginResponse'
service_name = 'LoginInterface' 
wsdl_port_name =  'ServiceLoginSOAP'
wsdl_port_binding = 'tns:ServiceLoginSoapBinding'


def generate_wsdl(
target_namespace,
definitions_name,
attributeFormDefault,
elementFormDefault,
element_name,
sub_element_name,
sub_element_type,
message_name,
part_element,
part_name,
port_type_name,
operation_name,
operation_input_name,
operation_input_message,
binding_name,
binding_type,
soap_binding_style,
wsdl_operation_name,
soap_operation_style,
wsdl_input_name,
soap_body_use,
wsdl_output_name,
operation_output_name,
service_name,
wsdl_port_name,
operation_output_message,
wsdl_port_binding,
element_count,
):

    WSDLNS = 'http://schemas.xmlsoap.org/wsdl/'
    XSDNS = 'http://www.w3.org/2001/XMLSchema'
    XSNS = 'http://www.w3.org/2001/XMLSchema'
    SOAPNS = 'http://schemas.xmlsoap.org/soap/http'

    definitions = etree.Element("{%s}definitions" % WSDLNS, nsmap={'wsdl': WSDLNS, 'xsd': XSDNS, 'tns': target_namespace, 'ns1': SOAPNS}, name=definitions_name, targetNamespace=target_namespace)
    types = etree.SubElement(definitions, "{%s}types" % WSDLNS)
    schema = etree.SubElement(types, "{%s}schema" % XSNS, attributeFormDefault=attributeFormDefault, elementFormDefault=elementFormDefault, targetNamespace=target_namespace, nsmap={'xs': XSNS, 'tns': target_namespace})
    element = etree.SubElement(schema, "{%s}element" % XSNS, name=element_name)
    complexType = etree.SubElement(element, "{%s}complexType" % XSNS)
    sequence = etree.SubElement(complexType, "{%s}sequence" % XSNS)
    sub_element = etree.SubElement(sequence, "{%s}element" % XSNS, name=sub_element_name, type=sub_element_type)
    message = etree.SubElement(definitions, "{%s}message" % WSDLNS,name=message_name)
    part = etree.SubElement(message, "{%s}part" % WSDLNS, element=part_element, name=part_name)
    port_type = etree.SubElement(definitions, "{%s}portType" % WSDLNS,name=port_type_name)
    operation = etree.SubElement(port_type, "{%s}operation" % WSDLNS,name=operation_name)
    operation_input = etree.SubElement(operation, "{%s}input" % WSDLNS, name=operation_input_name, message=operation_input_message)
    operation_output = etree.SubElement(operation, "{%s}output" % WSDLNS, name=operation_output_name, message=operation_output_message)
    wsdl_binding = etree.SubElement(definitions, "{%s}binding" % WSDLNS, name=binding_name, type=binding_type )
    soap_binding = etree.SubElement(wsdl_binding, "{%s}binding" % SOAPNS, style=soap_binding_style, transport=SOAPNS, nsmap={'soap': SOAPNS})
    wsdl_operation = etree.SubElement(soap_binding, "{%s}operation" % WSDLNS, name=wsdl_operation_name)
    soap_operation = etree.SubElement(wsdl_operation, "{%s}operation" % SOAPNS, style=soap_operation_style, soapAction=target_namespace)
    wsdl_input = etree.SubElement(wsdl_operation, "{%s}input" % WSDLNS, name=wsdl_input_name)
    soap_body = etree.SubElement(wsdl_input, "{%s}body" % SOAPNS, use=soap_body_use)
    wsdl_output = etree.SubElement(wsdl_operation, "{%s}output" % WSDLNS, name=wsdl_output_name)
    soap_body = etree.SubElement(wsdl_output, "{%s}body" % SOAPNS, use=soap_body_use)
    wsdl_service = etree.SubElement(definitions, "{%s}service" % WSDLNS, name=service_name )
    wsdl_port = etree.SubElement(wsdl_service, "{%s}port" % WSDLNS, name=wsdl_port_name, binding=wsdl_port_binding)
    service_soap_address = etree.SubElement(wsdl_port, "{%s}address" % WSDLNS, location=target_namespace)
    
    return etree.tostring(definitions, xml_declaration=True, encoding='UTF-8', pretty_print=True)


def web_generate():
    with open('uploads/elements.csv', 'rb') as csvfile:
        csv_object = csv.reader(csvfile, delimiter='\n')
        for row in csv_object:
            if row[0].find('BusinessFunction') > 0  and row[0].find('Авторизация') > 0:
		return generate_wsdl(target_namespace = 'http://sample.ru/login',
definitions_name = 'LoginInterface',
attributeFormDefault = 'unqualified',
elementFormDefault = 'unqualified',
element_name = 'login',
sub_element_name = 'login',
sub_element_type = 'xs:string',
message_name = 'login',
part_element = 'tns:login',
part_name = 'parameters',
port_type_name = 'LoginInterface',
operation_name = 'login',
operation_input_name = 'login',
operation_input_message = 'tns:login',
operation_output_name = 'loginResponse',
operation_output_message = 'loginResponse',
binding_name = 'ServiceLoginSoapBinding',
binding_type = 'tns:LoginInterface',
soap_binding_style = 'document',
wsdl_operation_name = 'login',
soap_operation_style = 'document',
wsdl_input_name = 'login',
soap_body_use = 'literal',
wsdl_output_name = 'loginResponse',
service_name = 'LoginInterface' ,
wsdl_port_name =  'ServiceLoginSOAP',
wsdl_port_binding = 'tns:ServiceLoginSoapBinding',
element_count = 2
)
#result_file.close()
