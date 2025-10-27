        )
        # اللاعب والأشباح
        self.pacman.draw(self.screen)
        for g in self.ghosts:
            g.draw(self.screen)
        self.draw_hud()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == STATE_PLAYING:
                        self.state = STATE_PAUSED
                    elif self.state in (STATE_PAUSED, STATE_START):
                        pygame.quit()
                        sys.exit()
                if self.state == STATE_START and event.key == pygame.K_RETURN:
                    self.state = STATE_PLAYING
                elif self.state == STATE_PAUSED and event.key == pygame.K_RETURN:
                    self.state = STATE_PLAYING

    def update(self):
        if self.state == STATE_PLAYING:
            self.update_play()

    def draw(self):
        if self.state == STATE_START:
            self.draw_start_screen()
        elif self.state == STATE_PLAYING:
            self.draw_play()
        elif self.state == STATE_PAUSED:
            self.draw_play()
            pause = self.font_big.render("PAUSED", True, WHITE)
            rect = pause.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(pause, rect)
        elif self.state == STATE_GAMEOVER:
            self.screen.fill(BLACK)
            over = self.font_big.render("GAME OVER", True, RED)
            rect = over.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(over, rect)
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = PacmanGame()
    game.run()
