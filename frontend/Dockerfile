#CREADA PARA DESARROLLO
#--------------------------------------------------------------------------
# Ejemplo de Dockerfile para desarrollo
# FROM node:18-alpine AS development

# WORKDIR /app
# COPY package*.json ./
# RUN npm ci
# COPY . .

# EXPOSE 7000
# CMD ["npm", "run","dev", "--", "-p", "7000"]
# CMD ["npm", "run", "dev"]
#--------------------------------------------------------------------------

#----CREADA PARA PRODUCCION -------------

FROM node:18-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
    
FROM node:18-alpine AS runtime
    
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY --from=build /app/.next ./.next
COPY --from=build /app/public ./public
    
EXPOSE 3000
USER node
CMD ["npm", "start"]

#--------------------------------------------------------------------------

#--VIDEO---#
# FROM node:latest
# WORKDIR /app
# COPY package.json . 
# RUN npc
# COPY . .
# RUN npm run build
# CMD [ "npm", "run", "dev" ]