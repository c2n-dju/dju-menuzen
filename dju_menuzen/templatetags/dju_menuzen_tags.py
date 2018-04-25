# -*- coding: utf-8 -*-

from __future__ import with_statement

import datetime
from classytags.arguments import IntegerArgument, Argument, StringArgument
from classytags.core import Options
from classytags.helpers import InclusionTag
from django import template
from django.conf import settings
from django.core.urlresolvers import reverse, NoReverseMatch
from django.template.base import Node
from django.template.defaultfilters import date
from django.utils import timezone
from django.utils.six.moves.urllib.parse import unquote
from django.utils.translation import get_language
from menus.menu_pool import menu_pool
from menus.utils import DefaultLanguageChanger


register = template.Library()


class ShowMenuZen(InclusionTag):
    """
    Shows the menu_zen from the node that has the same url as the current request

    - start_level: after which level should the breadcrumb start? 0=home
    - template: template used to render the breadcrumb
    """
    name = 'show_menuzen'
    template = 'menu/dummy.html'

    options = Options(
        Argument('start_level', default=0, required=False),
        Argument('template', default='menu/breadcrumb.html', required=False),
        Argument('only_visible', default=True, required=False),
    )

    def get_context(self, context, start_level, template, only_visible):
        try:
            # If there's an exception (500), default context_processors may not be called.
            request = context['request']
        except KeyError:
            return {'template': 'cms/content.html'}
        if not (isinstance(start_level, int) or start_level.isdigit()):
            only_visible = template
            template = start_level
            start_level = 0
        try:
            only_visible = bool(int(only_visible))
        except:
            only_visible = bool(only_visible)
        branch = []
        menu_renderer = context.get('cms_menu_renderer')
        if not menu_renderer:
            menu_renderer = menu_pool.get_renderer(request)
        nodes = menu_renderer.get_nodes(request, breadcrumb=False) # fait appel à deepcopy, False pour appeler AuthVisibility.modify
        selected = None
        home = None
        homeurl = unquote(reverse("pages-root"))
        debug_allnodes = []
        for node in nodes:
            #print()
            #print(node.title)
            #print(node.visible)
            #print(node.attr)
            # debug_allnodes.append((node.title, node.selected))
            if node.selected:
                selected = node
            if node.get_absolute_url() == homeurl:
                home = node
        if selected: #and selected != home:
            node = selected
            childnode = None
            level = 0
            color = 100
            while node:
                node.attr['color'] = "bread-" + str(color)
                if node == home:
                    node.attr['color'] = "bread-100"
                if level < 3:
                    color -= 20
                    node.attr['display'] = node.title
                else:
                    node.attr['display'] = '…'
                childs = []
                for c in node.children:
                    if c != childnode:
                        c.attr['display'] = node.title
                        c.attr['color'] = ''
                    childs.append(c)
                node.attr['childs'] = childs
                if node.visible or not only_visible:
                    branch.append(node)
                level += 1
                childnode = node
                node = node.parent
        if not branch or (branch and branch[-1] != home) and home:
            branch.append(home)
        branch.reverse()
        if len(branch) >= start_level:
            branch = branch[start_level:]
        else:
            branch = []
        context.update({'branch': branch,
                        'template': template,
                        'homeurl': homeurl,
                        'allnodes': debug_allnodes})
        return context


register.tag(ShowMenuZen)
