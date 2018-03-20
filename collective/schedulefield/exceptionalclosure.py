# -*- coding: utf-8 -*-
from z3c.form.browser.widget import HTMLFormElement
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.object import ObjectWidget
from z3c.form.widget import FieldWidget
from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implements
from zope.schema.interfaces import IObject


class IExceptionalClosure(IObject):
    """IExceptionalClosure"""


class ExceptionalClosure(schema.Object):
    implements(IExceptionalClosure)


class ExceptionalClosureWidget(HTMLFormElement, ObjectWidget):
    implements(IExceptionalClosure)

    klass = u'object-widget'
    css = u'object'


@adapter(IObject, IFormLayer)
@implementer(IFieldWidget)
def ObjectFieldWidget(field, request):
    """IFieldWidget factory for IObjectWidget."""
    return FieldWidget(field, ExceptionalClosureWidget(request))
