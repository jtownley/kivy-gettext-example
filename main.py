from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.label import Label

from os.path import join, dirname
import gettext


def _(string):
    '''This is just so we can use the default gettext format'''
    return string


class I18NLabel(Label):
    '''Example of a extended object using source_text'''
    source_text = StringProperty('')


class MySpecialLabel(I18NLabel):
    '''Example of programatic text'''
    def __init__(self, **kwargs):
        super(MySpecialLabel, self).__init__(**kwargs)
        self.source_text = _('Running')


class LangApp(App):
    lang = StringProperty('en')
    translation = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        self.switch_lang(self.lang)
        super(LangApp, self).__init__(**kwargs)

    def on_lang(self, instance, lang):
        self.switch_lang(lang)

    def switch_lang(self, lang):
        locale_dir = join(dirname(__file__), 'data', 'locales')
        locales = gettext.translation('langapp', locale_dir, languages=[self.lang])
        self.translation = locales.ugettext


LangApp().run()
