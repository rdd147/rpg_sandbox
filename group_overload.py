import pygame

class Group_off(pygame.sprite.Group):
    def draw(self, surface, offset = [0,0]):
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        for s in self.sprites():
            r = spritedict[s]
            newrect = surface_blit(s.image, s.rect.move(offset))
            if r is 0:
                dirty_append(newrect)
            else:
                if newrect.colliderect(r):
                    dirty_append(newrect.union(r))
                else:
                    dirty_append(newrect)
                    dirty_append(r)
            spritedict[s] = newrect
        return dirty