from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = 'mainapp/main.html'

    def get_template_names(self):
        lang = self.kwargs.get('lang', 'ru')
        if lang == 'ru':
            return ['mainapp/main.html']
        elif lang == 'en':
            return ['mainapp/main_en.html']
        elif lang == 'uz':
            return ['mainapp/main_uz.html']
        else:
            return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lang = self.kwargs.get('lang', 'ru')
        context['language'] = lang
        context['langs'] = {
            'ru': "Русский",
            'en': "English",
            "uz": "O'zbek"
        }
        if lang == 'ru':
            context['title'] = 'Ekogumus | УДОБРЕНИЯ ДЛЯ БОГАТОГО УРОЖАЯ!'
        if lang == 'en':
            context['title'] = 'Ekogumus | FERTILIZERS FOR A RICH HARVEST!'
        if lang == 'uz':
            context['title'] = "Ekogumus | BOY HOSILDORLIK UCHUN O'G'ITLAR!"
        return context


class AboutCompanyPageView(TemplateView):
    template_name = 'mainapp/about_company.html'

    def get_template_names(self):
        lang = self.kwargs.get('lang', 'ru')
        if lang == 'ru':
            return ['mainapp/about_company.html']
        elif lang == 'en':
            return ['mainapp/about_company_en.html']
        elif lang == 'uz':
            return ['mainapp/about_company_uz.html']
        else:
            return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lang = self.kwargs.get('lang', 'ru')
        context['language'] = lang
        context['langs'] = {
            'ru': "Русский",
            'en': "English",
            "uz": "O'zbek"
        }
        if lang == 'ru':
            context['title'] = 'Ekogumus | О компании'
        if lang == 'en':
            context['title'] = 'Ekogumus | About the Company'
        if lang == 'uz':
            context['title'] = "Ekogumus | Tashkilot haqida"
        return context


class ProductPageView(TemplateView):
    template_name = 'mainapp/product.html'

    def get_template_names(self):
        lang = self.kwargs.get('lang', 'ru')
        if lang == 'ru':
            return ['mainapp/product.html']
        elif lang == 'en':
            return ['mainapp/product_en.html']
        elif lang == 'uz':
            return ['mainapp/product_uz.html']
        else:
            return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lang = self.kwargs.get('lang', 'ru')
        context['language'] = lang
        context['langs'] = {
            'ru': "Русский",
            'en': "English",
            "uz": "O'zbek"
        }
        if lang == 'ru':
            context['title'] = 'Ekogumus | Продукция'
        if lang == 'en':
            context['title'] = 'Ekogumus | Product'
        if lang == 'uz':
            context['title'] = "Ekogumus | Mahsulot"
        return context


class CooperationPageView(TemplateView):
    template_name = 'mainapp/cooperation.html'

    def get_template_names(self):
        lang = self.kwargs.get('lang', 'ru')
        if lang == 'ru':
            return ['mainapp/cooperation.html']
        elif lang == 'en':
            return ['mainapp/cooperation_en.html']
        elif lang == 'uz':
            return ['mainapp/cooperation_uz.html']
        else:
            return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lang = self.kwargs.get('lang', 'ru')
        context['language'] = lang
        context['langs'] = {
            'ru': "Русский",
            'en': "English",
            "uz": "O'zbek"
        }
        if lang == 'ru':
            context['title'] = 'Ecogumus | Сотрудничество'
        if lang == 'en':
            context['title'] = 'Ecogumus | Cooperation'
        if lang == 'uz':
            context['title'] = "Ecogumus | Hamkorlik"
        return context


class NewsPageView(TemplateView):

    template_name = 'mainapp/news.html'
    
    def get_template_names(self):
        lang = self.kwargs.get('lang', 'ru')
        if lang == 'ru':
            return ['mainapp/news.html']
        elif lang == 'en':
            return ['mainapp/news_en.html']
        elif lang == 'uz':
            return ['mainapp/news_uz.html']
        else:
            return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lang = self.kwargs.get('lang', 'ru')
        context['language'] = lang
        context['langs'] = {
            'ru': "Русский",
            'en': "English",
            "uz": "O'zbek"
        }
        if lang == 'ru':
            context['title'] = 'Ecogumus | Новости'
        if lang == 'en':
            context['title'] = 'Ecogumus | News'
        if lang == 'uz':
            context['title'] = "Ecogumus | Yangiliklar"
        return context
    

class OneNewsPageView(TemplateView):
    template_name = 'mainapp/news_2.html'
    def get_template_names(self):
        lang = self.kwargs.get('lang', 'ru')
        if lang == 'ru':
            return ['mainapp/news_2.html']
        elif lang == 'en':
            return ['mainapp/news_2_en.html']
        elif lang == 'uz':
            return ['mainapp/news_2_uz.html']
        else:
            return super().get_template_names()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lang = self.kwargs.get('lang', 'ru')
        context['language'] = lang
        context['langs'] = {
            'ru': "Русский",
            'en': "English",
            "uz": "O'zbek"
        }
        if lang == 'ru':
            context['title'] = 'Ecogumus | Новости'
        if lang == 'en':
            context['title'] = 'Ecogumus | News'
        if lang == 'uz':
            context['title'] = "Ecogumus | Yangiliklar"
        return context